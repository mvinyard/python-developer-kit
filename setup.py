from setuptools import setup
import re
import os
import sys


setup(
    name="pydk",
    version="0.0.55",
    python_requires=">3.7.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url="https://github.com/mvinyard/python-developer-kit",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="Python Developer Kit",
    packages=[
        "pydk",
        "pydk._conda_package_installer",
    ],
    # These are all imported at import time by `pydk`, but only licorice_font
    # was declared. They happened to be present in the scientific environments
    # pydk is normally installed into, which masked the problem -- until pandas
    # 3.0 moved pytz from a hard dependency to an optional extra, at which point
    # `import pydk` began failing with ModuleNotFoundError on a clean install.
    install_requires=[
        "licorice_font>=0.0.3",
        "pytz>=2020.1",  # pydk/_current_time.py
        "numpy",  # pydk/_rounding.py, _find_overlapping.py, _filter_overlapping.py
        "pandas",  # pydk/_GIF.py, _conda_package_installer/_supporting_functions.py
        "pillow",  # pydk/_GIF.py (imported as PIL)
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
