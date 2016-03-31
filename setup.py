try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Intercom Project',
    'author': 'Ioannis N.',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['intercom'],
    'scripts': [],
    'name': 'customers'
}

setup(**config)
