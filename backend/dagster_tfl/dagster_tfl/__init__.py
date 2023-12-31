import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets.duck_dbt_assets import duck_dbt_dbt_assets
from .assets.constants import dbt_project_dir
from .schedules.schedules import schedules

defs = Definitions(
    assets=[duck_dbt_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)