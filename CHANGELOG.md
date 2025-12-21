# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org),
with the exception that all versions are currently `0.x.x` and may include breaking changes.

---

## [Unreleased]

### Added

- Added possibility for additional headers and proxies (handled by requests lib)
- Documentation for all functions

### Breaking Changes

- Renamed get_blogs_time() to get_blogs_for_year_month()

### Changed

- Use response headers to determine whether to parse HTTP responses into JSON
- get() can also return `list` type as JSON can also be a list

### Fixed

`N/A`

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
