#!/usr/bin/env bash

set -euo pipefail

rename_case() {
    local old="$1"
    local new="$2"

    if [[ -f "$old" ]]; then
        local tmp="${old}.tmp.$$"
         mv "$old" "$tmp"
         mv "$tmp" "$new"
        echo "Renamed: $old -> $new"
    else
        echo "Skipping: $old (not found)"
    fi
}

rename_case "docs/readme.md"        "docs/README.md"
rename_case "docs/architecture.md"  "docs/Architecture.md"
rename_case "docs/roadmap.md"       "docs/RoadMap.md"
rename_case "docs/contributing.md"  "docs/CONTRIBUTING.md"
rename_case "docs/changelog.md"     "docs/CHANGELOG.md"
rename_case "docs/protocol.md"      "docs/Protocol.md"
rename_case "docs/plugin-api.md"    "docs/PluginAPI.md"
rename_case "docs/device-api.md"    "docs/DeviceAPI.md"
rename_case "docs/capabilities.md"  "docs/Capabilities.md"
rename_case "docs/hardware.md"      "docs/Hardware.md"

echo
echo "Done!"
echo "Review with:"
echo "  git status"