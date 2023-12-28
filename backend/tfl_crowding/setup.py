from setuptools import find_packages, setup

setup(
    name="tfl_crowding",
    packages=find_packages(exclude=["tfl_crowding_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
