from .entry import DaylightFactorEntryPoint

__queenbee__ = {
    'name': 'daylight-factor',
    'entry_point': DaylightFactorEntryPoint,
    'description': 'Daylight factor recipe for Pollination.',
    'icon': 'https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_components/honeybee/png/dfrecipe.png',
    'tag': '0.3.0',  # tag for honeybee-radiance plugin
    'app_version': '5.4',  # tag for version of Radiance
    'keywords': ['honeybee', 'radiance', 'ladybug-tools', 'daylight'],
    'maintainers': [
        {'name': 'mostapha', 'email': 'mostapha@ladybug.tools'}
    ],
    'license': {
        'name': 'PolyForm Shield License 1.0.0',
        'url': 'https://polyformproject.org/wp-content/uploads/2020/06/PolyForm-Shield-1.0.0.txt'
    }
}
