from setuptools import setup
try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup, find_packages


setup(
    name='GSjupies',

    version='0.0.0',

    description='A user self interative genome-analysis tool based on jupyter notebook, which supports raw data from 23Mofang, 23andme etc.',

    author='Oasis Ye',

    packages=find_packages(),

    install_requires=['ipywidgets',
                      'qgrid',
                      'plotly',
                      'scipy'
                      ]

)