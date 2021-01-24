#!/usr/bin/env python
from setuptools import find_packages, setup

# add these line to integrate the queenbee packaging process
# into Python packaging
from queenbee_dsl.package import PackageQBInstall, PackageQBDevelop
name = 'annual-energy-use'
PackageQBInstall.__queenbee_name__ = name
PackageQBDevelop.__queenbee_name__ = name

setup(
    cmdclass={
        'develop': PackageQBDevelop,
        'install': PackageQBInstall
    },
    name=name,
    author='chris',
    author_email='chris@ladybug.tools',
    description="Run an annual energy simulation and compute energy use intensity.",
    setup_requires=['setuptools_scm'],
    packages=find_packages('annual_energy_use'),
    keywords=['honeybee', 'energyplus', 'openstudio', 'ladybug-tools', 'energy'],
    license='PolyForm Shield License 1.0.0',
    python_requires=">=3.7"
)
