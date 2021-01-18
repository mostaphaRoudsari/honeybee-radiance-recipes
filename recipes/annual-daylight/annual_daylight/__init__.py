from .entry import AnnualDaylightEntryPoint

__queenbee__ = {
    'name': 'annual-daylight',
    'entry_point': AnnualDaylightEntryPoint,
    'description': 'Annual daylight recipe for Pollination.',
    'icon': 'https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_components/honeybee/png/annualrecipe.png',
    'tag': '0.2.1',  # tag for annual daylight recipe
    'app_version': '5.4',  # tag for version of Radiance
    'keywords': [
        'honeybee', 'radiance', 'ladybug-tools', 'daylight', 'daylight autonomy',
        'useful daylight illuminance'
        ],
    'maintainers': [
        {'name': 'mostapha', 'email': 'mostapha@ladybug.tools'}
    ],
    'license': {
        'name': 'PolyForm Shield License 1.0.0',
        'url': 'https://polyformproject.org/wp-content/uploads/2020/06/PolyForm-Shield-1.0.0.txt'
    }
}
