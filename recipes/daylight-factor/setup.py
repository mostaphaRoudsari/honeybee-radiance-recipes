#!/usr/bin/env python
from setuptools import find_packages, setup

# add these line to integrate the queenbee packaging process
# into Python packaging
from queenbee_dsl.package import PackageQBInstall, PackageQBDevelop
name = 'daylight-factor'
PackageQBInstall.__queenbee_name__ = name
PackageQBDevelop.__queenbee_name__ = name

setup(
    cmdclass={
        'develop': PackageQBDevelop,
        'install': PackageQBInstall
    },
    name=name,
    author='mostapha',
    author_email='mostapha@ladybug.tools',
    description="Daylight factor simulation implementation as a Queenbee recipe.",
    setup_requires=['setuptools_scm'],
    packages=find_packages('daylight_factor'),
    keywords=['honeybee', 'radiance', 'ladybug-tools', 'daylight'],
    license='PolyForm Shield License 1.0.0',
    python_requires=">=3.7"
)
