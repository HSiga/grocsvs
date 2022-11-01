from setuptools import setup, find_packages

def get_version(path):
    """ Parse the version number variable __version__ from a script. """
    import re
    string = open(path).read()
    version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_str = re.search(version_re, string, re.M).group(1)
    return version_str


setup(
    name = 'grocsvs',
    version = get_version("src/grocsvs/__init__.py"),

    packages = find_packages('src'),
    package_dir = {"": "src"},

    entry_points = {
        'console_scripts' : ["grocsvs = grocsvs.main:main"]
    },

    install_requires = ["admiral==0.1", "h5py==2.6.0", "pandas>=0.19.2", "networkx==2.0",
                        "pip>=9.0.1", "rpy2==2.8.6", "decorator==4.3", "ipython-cluster-helper==0.5.4",
                        "pyfaidx==0.4.8.2", "pysam>=0.10.0", "scipy==0.19.0", "psutil==5.2.1"],

)
