A python library for querying and updating a stash sqlite database

pystashlib and Stash compatibility table:
| pystashlib | Stash version | Stash schema |
| ------------- | ------------- | ------------- |
| v0.6.0 | v0.27.0 | 67 |
| v0.5.0 | v0.25.0-v0.25.1 | 55 |
| v0.4.0-v0.4.5 | v0.24.0-v0.24.3 | 54 |
| v0.3.0-v0.3.1 | v0.17.0-v0.17.2 | 36 |
| v0.2.8 | v0.15.0-v0.16.1 | 31 |
| v0.2.7 | v0.14.0 | 30 |
| v0.2.5 | v0.12.0-v0.13.1 | 29 |
| v0.2.4 | v0.11.0 | 28 |

# Changelog

## v0.6.0
* Update to support Stash v0.27.0

## v0.5.0
* Update to support Stash v0.25.0

## v0.4.5
* Add `requests` package to list of requirements

## v0.4.4
* Updated StashInterface GQL client to support Stash v0.24.3

## v0.4.3
*  Added support for performer name disambiguation

### Changed
* `query_performer_name` Returns list[PerformersRow] instead of PerformersRow.
* `create_performer_from_url` Added disambiguation argument

   `def create_performer_from_url(self, name, disambiguation, url, commit=True):`

### Added
* `query_performer_name_disambiguated` Returns a PerformersRow match on name and disambiguation.

   Pass None or "" to get a PerformersRow with no disambiguation.

## v0.4.2
*  Added back tree_from_file and scrape functions to new stashlib.html module with lxml as an optional dependency

## v0.4.1
* Fix image blob saving

## v0.4.0
* Update to support Stash v0.24.3

## v0.3.1
* Removed tree_from_file and scrape functions from stashlib.common to remove dependency on lxml