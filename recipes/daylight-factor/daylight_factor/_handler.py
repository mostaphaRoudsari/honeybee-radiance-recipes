from queenbee_dsl.alias import InputAlias, OutputAlias
from queenbee.io.common import IOAliasHandler


input_model_alias = [
    # grasshopper Alias
    InputAlias.any(
        name='model',
        description='A path to a HBJSON file or a HB model object built with Python or'
        'dotnet libraries.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python', module='honeybee_radiance_handlers.handlers',
                function='model_to_json_path'
            ),
            IOAliasHandler(
                language='csharp', module='HoneybeeSchema.Handlers',
                function='HBModelToJSON'
            )
        ]
    ),
    # Rhino alias
    InputAlias.linked(
        name='model',
        description='This input links the model to Rhino model.',
        platform=['rhino'],
        handler=[
            IOAliasHandler(
                language='csharp', module='HoneybeeRhino.Handlers',
                function='RhinoHBModelToJSON'
            )
        ]
    )

]


parse_daylight_factor_results = [
    OutputAlias.any(
        name='daylight_factor',
        description='Daylight factor values.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python', module='honeybee_radiance_handlers.handlers',
                function='read_DF_from_path'
            )
        ]
    )
]
