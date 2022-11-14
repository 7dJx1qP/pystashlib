import base64
import cloudscraper
import hashlib
import json
import math
import os
import re
import time
import yaml
from datetime import date, datetime, timedelta
from dateutil.tz import tzoffset
from .logger import logger as log

def alpha_chars(s):
    return ''.join([c for c in s if c.isalpha()])

def alphanum_chars(s):
    return ''.join([c for c in s if c.isalnum()])

def camel_case(s):
    return ''.join(word.title() for word in s.split('_'))
        
def array_param(l):
    return ', '.join('?'*len(l))

def dict_subset(d, keys):
    return {key: d[key] for key in keys}

def get_checksum(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def get_timestamp():
    return datetime.now(tzoffset('EDT', -4*60*60)).replace(microsecond=0).isoformat()

def get_timestamp_str():
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

def image_to_base64(content):
    b64img = base64.b64encode(content)
    return "data:image/jpeg;base64," + b64img.decode('utf-8')

def url2filename(url):
    url = url.encode('UTF-8')
    return base64.urlsafe_b64encode(url).decode('UTF-8')

def filename2url(f):
    return base64.urlsafe_b64decode(f).decode('UTF-8')

def optional_nonalphanum_regex(s):
    return '(?i)' + ''.join([ch if ch.isalnum() or ch == '\\' else ch + '*' for ch in re.escape(s)])

def strip_end(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text

def scrape_image(url):
    log.LogDebug(f'scrape_image {url}')
    while True:
        scraper = cloudscraper.create_scraper()
        try:
            scraped = scraper.get(url, timeout=(3,7))
        except Exception as e:
            log.LogDebug("scrape error %s" %e )
        if scraped.status_code < 400:
            break
        else:
            log.LogDebug("HTTP error %s" % scraped.status_code)
        time.sleep(2)
    return scraped.content

PARTPATTERN = re.compile('(.*?)(?:-poster|-fanart)*(?: part(\d+))*$')

def parse_part(name):
    m = re.search(PARTPATTERN, name)
    if m:
        try:
            part = int(m.group(2))
        except:
            part = 1
        return part, m.group(1)
    else:
      return 1, name

def file_read_lines(filepath, encoding='utf8'):
    with open(filepath, 'r', encoding=encoding) as f:
        return [x.strip() for x in f.readlines()]

def file_write_lines(lines, filepath):
    with open(filepath, 'w') as f:
        for line in lines:
            f.write(str(line) + '\n')

def file_write_line_groups(groups, filepath):
    lines = []
    for group in groups:
        lines += group
        lines.append('')
    file_write_lines(lines, filepath)

def file_read_line_groups(filepath, n=2, encoding='utf8'):
    results = []
    lines = file_read_lines(filepath, encoding)
    for i in range(0, len(lines), n + 1):
        items = []
        for j in range(0, n):
            items.append(lines[i + j])
        results.append(items)
    return results

def partition(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def load_json(filepath, default=None):
    if not default:
        default = {}
    dirpath = os.path.dirname(os.path.abspath(filepath))
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    try:
        return json.load(open(filepath, encoding='utf-8'))
    except Exception as e:
        log.LogError(str(e))
        if not os.path.exists(filepath):
            if default is not None:
                with open(filepath, 'w') as f:
                    f.write(json.dumps(default, ensure_ascii=True, sort_keys=True, indent=4))
        return default

def load_versioned_json(dirpath, default=None):
    if not default:
        default = {}
    if os.path.exists(dirpath) and os.listdir(dirpath):
        latest_file = os.path.join(dirpath, os.listdir(dirpath)[-1])
    else:
        latest_file = os.path.join(dirpath, get_timestamp_str() + '.json')
    return load_json(latest_file, default)

def save_json(filepath, data, ensure_ascii=True, sort_keys=True, indent=4):
    dirpath = os.path.dirname(os.path.abspath(filepath))
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, ensure_ascii=ensure_ascii, sort_keys=sort_keys, indent=indent))

def save_versioned_json(dirpath, data, ensure_ascii=True, sort_keys=True, indent=4):
    filepath = os.path.join(dirpath, get_timestamp_str() + '.json')
    save_json(filepath, data, ensure_ascii, sort_keys, indent)
    return filepath


def load_yaml(filepath, default=None):
    if not default:
        default = {}
    dirpath = os.path.dirname(os.path.abspath(filepath))
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    try:
        data = yaml.load(open(filepath), Loader=yaml.FullLoader)
        return data or default
    except:
        if not os.path.exists(filepath):
            if default is not None:
                with open(filepath, 'w') as f:
                    yaml.dump(default, f, default_flow_style=False)
        return default

def load_versioned_yaml(dirpath, default=None):
    if not default:
        default = {}
    if os.path.exists(dirpath) and os.listdir(dirpath):
        latest_file = os.path.join(dirpath, os.listdir(dirpath)[-1])
    else:
        latest_file = os.path.join(dirpath, get_timestamp_str() + '.yaml')
    return load_yaml(latest_file, default)

def save_yaml(filepath, data):
    dirpath = os.path.dirname(os.path.abspath(filepath))
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, width=1000**2)

def save_versioned_yaml(dirpath, data, ensure_ascii=True, sort_keys=True, indent=4):
    filepath = os.path.join(dirpath, get_timestamp_str() + '.yaml')
    save_yaml(filepath, data)
    return filepath

def split_path(filepath):
    dirpath, filename = os.path.split(filepath)
    file, ext = os.path.splitext(filename)
    part, name = parse_part(file)
    return name, ext, part, dirpath

def pretty_print_seconds(seconds):
    return str(timedelta(seconds=seconds))

def pretty_print_bytes(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s%s" % (s, size_name[i])

def parse_date_str(s):
    p1, p2, p3 = [int(x) for x in re.split('\.|\-|\_|\s', s.strip().removeprefix('(').removesuffix(')')) if x]
    current_yy = date.today().year - 2000
    year = None
    month = None
    day = None

    if p1 > current_yy and p1 <= 31:
        day = p1
        month = p2
        year = p3 % 2000 + 2000
        return f'{year}-{str(month).zfill(2)}-{day}'
    elif p2 > 12:
        day = p2
        month = p1
        year = p3 % 2000 + 2000
        return f'{year}-{str(month).zfill(2)}-{day}'
    elif p3 > current_yy and p3 <= 31:
        day = p3
        month = p2
        year = p1 % 2000 + 2000
        return f'{year}-{str(month).zfill(2)}-{day}'
    elif p1 >= 2000:
        day = p3
        month = p2
        year = p1 % 2000 + 2000
        return f'{year}-{str(month).zfill(2)}-{day}'

    if p1 == p3:
        year = p1 % 2000 + 2000

    if p1 > 12:
        month = p2

        if p1 == p3:
            day = p3
            month = p2
            year = p1 % 2000 + 2000
            return f'{year}-{str(month).zfill(2)}-{day}'
        
    if p3 >= 2000:
        year = p3 % 2000 + 2000
        
        if p1 > 12:
            day = p1
            return f'{year}-{str(month).zfill(2)}-{day}'
            
        elif p2 > 12:
            day = p2
            month = p1
            return f'{year}-{str(month).zfill(2)}-{day}'

        elif p1 == p2:
            day = p1
            month = p2
            return f'{year}-{str(month).zfill(2)}-{day}'

    return None