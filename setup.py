from setuptools import setup

 

setup(

    name='nyseconverter',

    version='0.1',

    description='NYSE converter',

    url='https://github.com/satyacom/file-format-converter.git',

    author='srinivas',

    author_email='satya@example.com',

    license='MIT',

    packages=['nyseconverter'],

    zip_safe=False,

    install_requires = [

        "dask[complete]"

    ],

    entry_points = {

        'console_scripts': ['nyseconverter=nyseconverter:main'],

    }

)