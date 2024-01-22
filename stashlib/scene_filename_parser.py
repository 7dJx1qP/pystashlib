import os
import re
from enum import StrEnum
from .common import parse_date_str
from .stash_database import StashDatabase

class S(StrEnum):
    studio = '\[(?P<studio>[a-zA-Z0-9]+)\]'
    title = '(?P<title>.*?)'
    performers = "(?P<performers>[a-zA-Z0-9 ,']+)"
    date = '\((?P<date>\d{2,4}\.\d\d\.\d{2,4})\)'

PATTERNS = [
    re.compile(f'^{S.studio} {S.performers} - {S.title} {S.date}$'),
    re.compile(f'^{S.studio} {S.performers} - {S.title}$'),
    re.compile(f'^{S.studio} {S.performers} {S.date}$'),
    re.compile(f'^{S.studio} {S.performers}$'),
    re.compile(f'^{S.performers} - {S.title} {S.date}$'),
    re.compile(f'^{S.performers} - {S.title}$'),
    re.compile(f'^{S.title} {S.date}$'),
]

def parse_filename(filename, pattern=None):
    studio = None
    performers = []
    title = None
    date = None
    if pattern:
        patterns = [re.compile(pattern)]
    else:
        patterns = PATTERNS
    for pattern in patterns:
        m = pattern.match(filename)
        if m:
            groups = m.groupdict()
            if 'studio' in groups:
                studio = groups['studio'].strip()
            if 'performers' in groups:
                performers = [x.strip() for x in groups['performers'].split(', ')]
            if 'title' in groups:
                title = groups['title'].strip()
            if 'date' in groups:
                date = groups['date'].replace('.', '-')
            return True, studio, performers, title, date
            break
    return False, studio, performers, title, date

def parse_scene_filename(filepath):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    return parse_filename(filename)

class SceneMapping(object):
    def __init__(self, filepath):
        self.filepath = filepath
        studio, title, names, date = parse_scene_filename(filepath)
        self.file_studio = studio
        self.file_title = title
        self.file_performer_names = names
        self.file_date = date
        self.studio = []
        self.performers = {}
        self.date = parse_date_str(date)

    def map_from_database(self, db: StashDatabase):
        if self.file_studio:
            self.studio = db.query_studio_name_regex(self.file_studio)
        for name in self.file_performer_names:
            self.performers[name] = db.query_performer_name_regex(name)

    def to_dict(self):
        data = {
            'filepath': self.filepath,
            'studio': [studio.name for studio in self.studio],
            'performers': {},
            'date': self.date,
        }
        for file_performer_name, performers in self.performers.items():
            data['performers'][file_performer_name] = []
            if not performers:
                data['performers'][file_performer_name].append({
                    'name': '',
                    'url': ''
                })
            for performer in performers:
                data['performers'][file_performer_name].append({
                    'name': performer.name,
                    'url': performer.url
                })
        return data

    def from_dict(self, data, db: StashDatabase):
        self.filepath = data['filepath']
        for studio_name in data['studio']:
            studio = db.studios.selectone_name(studio_name)
            if studio:
                self.studio.append(studio)
        for file_performer_name, performer_data in data['performers'].items():
            performer = db.performers.selectone_name(performer_data['name'])
            if performer:
                self.performers.append(performer)
        

def map_scene_filename(db: StashDatabase, filepath):
    scene_mapping = SceneMapping(filepath)

    return scene_mapping