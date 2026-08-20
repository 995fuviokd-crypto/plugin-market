import json, os, zipfile

SRC = "/tmp/plugin-market/plugins-src"
OUT = "/tmp/plugin-market/plugins"
REPO = "995fuviokd-crypto/plugin-market"

entries = []
for name in sorted(os.listdir(SRC)):
    d = os.path.join(SRC, name)
    if not os.path.isdir(d):
        continue
    with open(os.path.join(d, "plugin.json"), encoding="utf-8") as f:
        info = json.load(f)
    zname = f"{info['id']}-{info['version']}.zip"
    with zipfile.ZipFile(os.path.join(OUT, zname), "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(d):
            for fn in files:
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, d)
                z.write(full, rel)
    entries.append({
        "id": info["id"],
        "name": info["name"],
        "version": info["version"],
        "description": info.get("description", ""),
        "author": info.get("author", ""),
        "category": info.get("category", "general"),
        "repository": info.get("repository", ""),
        "downloadUrl": f"https://github.com/{REPO}/raw/main/plugins/{zname}",
        "type": info.get("type", "plugin"),
        "tags": info.get("tags", []),
    })

with open("/tmp/plugin-market/plugins.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"{len(entries)} plugins indexed")
for e in entries:
    print(" ", e["id"], e["version"], e["type"])
