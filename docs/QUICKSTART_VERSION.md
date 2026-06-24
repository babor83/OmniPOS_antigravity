# Version Control - Quick Start Guide

## Quick Reference

### Check Current Versions

```bash
# Application version
cd /home/ubuntu/frappe-bench
bench --site nexus.local execute omnipos.utils.get_app_version
# Output: "1.0.0"

# Build version (for cache busting)
bench --site nexus.local execute omnipos.utils.get_build_version
# Output: "1730569908806"
```

### Bump Version

```bash
cd /home/ubuntu/frappe-bench/apps/omnipos

# Patch release (1.0.0 → 1.0.1) - Bug fixes
./scripts/version-bump.sh patch

# Minor release (1.0.0 → 1.1.0) - New features
./scripts/version-bump.sh minor

# Major release (1.0.0 → 2.0.0) - Breaking changes
./scripts/version-bump.sh major
```

### After Version Bump

```bash
# 1. Build frontend (generates new version.json)
cd POS
yarn build

# 2. Verify build version
cat ../omnipos/public/pos/version.json

# 3. Commit and tag
git add .
git commit -m "chore: bump version to 1.0.1"
git tag v1.0.1
git push origin develop --tags
```

## File Locations

- **App Version**: `omnipos/__init__.py` → `__version__ = "1.0.0"`
- **Frontend Version**: `POS/package.json` → `"version": "1.0.0"`
- **Build Version**: `omnipos/public/pos/version.json` (generated during build)
- **Version Utilities**: `omnipos/utils.py`
- **Bump Script**: `scripts/version-bump.sh`

## Common Tasks

### Create a New Release

```bash
# 1. Bump version
./scripts/version-bump.sh patch

# 2. Build
cd POS && yarn build

# 3. Test locally
cd /home/ubuntu/frappe-bench
bench --site nexus.local execute omnipos.utils.get_build_version

# 4. Commit and tag
git add .
git commit -m "chore: release v1.0.1"
git tag v1.0.1
git push origin develop --tags
```

### Force Cache Refresh

When you need users to get the latest assets immediately:

```bash
# 1. Build with new version
cd POS
yarn build

# 2. Verify new build version was generated
cat ../omnipos/public/pos/version.json

# 3. Restart bench (optional, for backend changes)
cd /home/ubuntu/frappe-bench
bench restart
```

### Verify Version Setup

```bash
# Check all version files exist
ls -la omnipos/__init__.py
ls -la POS/package.json
ls -la omnipos/public/pos/version.json

# Check versions match
grep "__version__" omnipos/__init__.py
grep "version" POS/package.json
cat omnipos/public/pos/version.json
```

## Version Strategy

- **PATCH** (1.0.X): Bug fixes, small improvements
- **MINOR** (1.X.0): New features, backwards-compatible
- **MAJOR** (X.0.0): Breaking changes, major updates

## Troubleshooting

**Issue**: Version not updating in browser
```bash
# Solution: Clear cache and rebuild
cd POS
rm -rf ../omnipos/public/pos/*
yarn build
```

**Issue**: get_build_version returns fallback format `1.0.0-timestamp`
```bash
# Solution: version.json is missing, rebuild frontend
cd POS
yarn build
```

**Issue**: Version bump script fails
```bash
# Solution: Check file permissions
chmod +x scripts/version-bump.sh
./scripts/version-bump.sh patch
```

## More Information

See `VERSION_CONTROL.md` for comprehensive documentation.
