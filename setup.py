"""This is a setup.py script to install ModeMap as a package."""

import os
from setuptools import setup, find_packages

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))


setup(
    name="ModeMap",
    packages=find_packages(),
    version="0.0.1",
    install_requires=[
        "scipy",
        "phonopy",
    ],
    license="MIT",
    entry_points={
        'console_scripts': [
            'ModeMap=ModeMap',
            'ExtractTotalEnergies=ExtractTotalEnergies',
            'ModeMap_PostProcess=ModeMap_PostProcess',
            'ModeMap_PolyFit=ModeMap_PolyFit'
        ],
})
