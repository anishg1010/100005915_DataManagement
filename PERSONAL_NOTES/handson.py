from pathlib import Path
from urllib.request import urlretrieve

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/MehrdadJalali-AI/data-management-teaching-materials/main"

required_files = [
    ("data/metadata/climate_dataset_dublin_core.xml", "data/metadata/climate_dataset_dublin_core.xml"),
]

for local_rel, github_rel in required_files:
    local_path = Path(local_rel)
    if not local_path.exists():
        local_path.parent.mkdir(parents=True, exist_ok=True)
        url = f"{GITHUB_RAW_BASE}/{github_rel}"
        urlretrieve(url, local_path)
        print(f"Downloaded: {local_path}")
    else:
        print(f"Already available: {local_path}")

print("Bootstrap complete.")