from pathlib import Path
import os

from setuptools import setup, Extension
from Cython.Build import cythonize

BASE = Path(__file__).resolve().parent
os.chdir(BASE)

extensions = [
    Extension("screenshot", ["screenshot.py"]),
    Extension("utils", ["utils.py"]),
    Extension("screenshot", ["screenshot.py"]),
    Extension("main", ["main.py"]),
    Extension("detect_sleep", ["detect_sleep.py"]),
    Extension("const", ["const.py"]),
    Extension("capture_window", ["capture_window.py"]),
]


setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",           
        },
        
    )
)