from setuptools import setup, find_packages

setup(
    name='pytest_qanova',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'pytest11': [
            'pytest_qanova = pytest_qanova.plugin',
            ],
        },
    install_requires=[
        'pytest',
        ],
    )
