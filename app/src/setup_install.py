from setuptools import setup, find_packages

setup(
    name="get_temperatura_api",
    version="0.0.1",
    packages=find_packages(),
    script_args=["bdist_egg"],
    install_requires=[
        "boto3",
        "json"
    ]
)
