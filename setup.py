from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'DefiChain exporter for Prometheus'
LONG_DESCRIPTION = 'DefiChain master node exporter for Prometheus'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="defichain-exporter", 
        version=VERSION,
        author="Christian Sandrini",
        author_email="mail@chrissandrini.ch",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'defichain', 'exporter'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
        entry_points = {
            "console_scripts": ["defichain-exporter=defichain_exporter.__main__:main"]
        }
)
