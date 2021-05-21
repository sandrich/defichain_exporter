from setuptools import setup, find_packages
from os import path

DESCRIPTION = 'DefiChain exporter for Prometheus'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="defichain_exporter", 
        version="0.0.1",
        author="Christian Sandrini",
        author_email="mail@chrissandrini.ch",
        url="https://github.com/sandrich/defichain_exporter",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=['jsonrpc_requests', 'prometheus-client'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'defichain', 'exporter'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux"
        ],
        entry_points = {
            "console_scripts": ["defichain-exporter=defichain_exporter.__main__:main"]
        }
)
