"""Get a set of public domain terrain icons from Worldographer to place on the map.
"""

import shutil
import tempfile
import zipfile
from os import mkdir
from os.path import exists
from urllib.request import urlretrieve

# icons = "https://worldographer.com/releases/multicolored-classic.zip"
icons = "https://worldographer.com/releases/bw-icons.zip"


def get_icons(tmpdir):
    zip_path = f"{tmpdir}/{icons.split('/')[-1]}"
    icon_path = "../caesar/assets/icons"
    if not exists(zip_path):
        urlretrieve(icons, zip_path)
    if not exists(icon_path):
        mkdir(icon_path)
    Z = zipfile.ZipFile(zip_path)
    _ = [shutil.copy2(Z.extract(f, tmpdir), icon_path) for f in Z.filelist if f.filename.endswith(".png")]


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        get_icons(tmpdir)
