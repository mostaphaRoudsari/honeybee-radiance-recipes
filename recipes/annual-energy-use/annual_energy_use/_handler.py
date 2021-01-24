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
                language='python', module='pollination_handlers.inputs.model',
                function='model_to_json'
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
