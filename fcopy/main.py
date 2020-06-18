#!/usr/bin/python3

import os
import shutil
from pathlib import Path

sourcePath = Path(os.path.expanduser("~/tmp/"))
targetPath = Path(os.path.expanduser("~/tmp/pytest"))

for sourceFilePath in sourcePath.glob("*/*.txt"):
    sourceFileDetail = sourceFilePath.relative_to(sourcePath)
    targetFilePath = targetPath / sourceFileDetail

    try:
        try:
            shutil.copy(sourceFilePath, targetFilePath)
        except FileNotFoundError:
            os.makedirs(str(targetFilePath.parent))
            shutil.copy(sourceFilePath, targetFilePath)
    except OSError as ex:
        print(ex)
