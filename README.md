A python library for querying and updating a stash sqlite database

pystashlib and Stash compatibility table:
| pystashlib | Stash version | Stash schema |
| ------------- | ------------- | ------------- |
| v0.4.0 | v0.24.3 | 54 |
| v0.3.0-v0.3.1 | v0.17.0-v0.17.2 | 36 |
| v0.2.8 | v0.15.0-v0.16.1 | 31 |
| v0.2.7 | v0.14.0 | 30 |
| v0.2.5 | v0.12.0-v0.13.1 | 29 |
| v0.2.4 | v0.11.0 | 28 |

# Changelog

## v0.3.1
* Removed tree_from_file and scrape functions from stashlib.common to remove dependency on lxml