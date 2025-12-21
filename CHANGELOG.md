# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org).
Since `1.0.0`, breaking changes will only be introduced in major versions.

---

## [Unreleased]

### Added

- Added `get_blogs_for_year()` which basically calls `get_blogs_for_year_month()` 12 times
- Added possibility for additional headers and proxies (handled by requests lib)
- `AccountClient` object created to interact with account API
- `get_available()` created to check if a username is taken
- Doc-strings for all functions

### Breaking Changes

- Renamed `get_blogs_time()` to `get_blogs_for_year_month()`
- `HytaleAPIError` now includes the HTTP response status code for improved debugging

### Changed

- Use response headers to determine whether to parse HTTP responses into JSON

### Fixed

- `get()` can also return `list` type as JSON can also be a list

---

## [1.0.1] - 2025-12-20

### Added

- get_link() implementation for all images to get the link to the image's CDN
- Greater depth in README.md explaining how to use basic functions

### Changed

`N/A`

### Fixed

- Store `Category` object in `Media` for a media's category instead of a `str`

---

## [1.0.0] - 2025-12-19

### Added

- BlogPost, BlogPostExcerpt and CoverImage models created
- get_blogs(), get_blog(), get_blogs_time() implemented
- Status model created and get_status() implemented
- All media types and category models created
- get_concept_arts(), get_desktop_wallpapers(), get_mobile_wallpapers(), get_screenshots() and get_videos() implemented
- Package model created and get_packages() implemented

### Changed

`N/A`

### Fixed

`N/A`
