from typing import Dict, List
from queenbee_dsl.dag import Inputs, DAG, task, Outputs
from dataclasses import dataclass
from pollination_honeybee_energy.settings import SimParDefault
from pollination_honeybee_energy.simulate import SimulateModel
from pollination_honeybee_energy.result import EnergyUseIntensity

from ._handler import input_model_alias


@dataclass
class AnnualEnergyUseEntryPoint(DAG):
    """Annual energy use entry point."""

    # inputs
    model = Inputs.file(
        description='A Honeybee model in HBJSON file format.',
        extensions=['json', 'hbjson'],
        alias=input_model_alias
    )

    epw = Inputs.file(
        description='EPW weather file to be used for the annual energy simulation.',
        extensions=['epw']
    )

    ddy = Inputs.file(
        description='A DDY file with design days to be used for the initial '
        'sizing calculation.', extensions=['ddy']
    )

    filter_des_days = Inputs.str(
        description='A switch for whether the ddy-file should be filtered to only '
        'include 99.6 and 0.4 design days', default='filter-des-days',
        spec={'type': 'string', 'enum': ['filter-des-days', 'all-des-days']}
    )

    units = Inputs.str(
        description='A switch to indicate whether the data in the final EUI file '
        'should be in SI (kWh/m2) or IP (kBtu/ft2). Valid values are "si" and "ip".',
        default='si', spec={'type': 'string', 'enum': ['si', 'ip']}
    )

    # tasks
    @task(template=SimParDefault)
    def create_sim_par(self, ddy=ddy, filter_des_days=filter_des_days) -> List[Dict]:
        return [
            {'from': SimParDefault()._outputs.sim_par_json,
             'to': 'simulation_parameter.json'}
            ]

    @task(template=SimulateModel, needs=[create_sim_par])
    def run_simulation(
        self, model=model, epw=epw,
        sim_par=create_sim_par._outputs.sim_par_json
    ) -> List[Dict]:
        return [
            {'from': SimulateModel()._outputs.hbjson, 'to': 'model.hbjson'},
            {'from': SimulateModel()._outputs.result_folder, 'to': 'run'}
            ]

    @task(template=EnergyUseIntensity, needs=[run_simulation])
    def compute_eui(
        self, result_folder=run_simulation._outputs.result_folder, units=units
    ) -> List[Dict]:
        return [
            {'from': EnergyUseIntensity()._outputs.eui_json,
             'to': 'eui.json'}
            ]

    # outputs
    eui = Outputs.file(
        source='eui.json', description='A JSON containing energy use intensity '
        'information across the total model floor area. Values are either kWh/m2 '
        'or kBtu/ft2 depending upon the units input.'
    )

    osm = Outputs.file(
        source='run/in.osm', description='The OpenStudio model used in the simulation.'
    )

    idf = Outputs.file(
        source='run/in.idf', description='The IDF model used in the simulation.'
    )

    sql = Outputs.file(
        source='run/eplusout.sql',
        description='The result SQL file output by the simulation.'
    )

    zsz = Outputs.file(
        source='run/epluszsz.csv', description='The result CSV with the zone loads '
        'over the design day output by the simulation.'
    )

    html = Outputs.file(
        source='run/eplustbl.htm',
        description='The result HTML page with summary reports output by the simulation.'
    )

    err = Outputs.file(
        source='run/eplusout.err',
        description='The error report output by the simulation.'
    )
