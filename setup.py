"""Setup for TcEx Module."""
# standard library
import os

# third-party
from setuptools import find_packages, setup

metadata = {}
metadata_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tcex', '__metadata__.py')
with open(
    metadata_file,
    encoding='utf-8',
) as f:
    exec(f.read(), metadata)  # nosec; pylint: disable=exec-used

if not metadata:
    raise RuntimeError(f'Could not load metadata file ({metadata_file}).')

with open('README.md') as f:
    readme = f.read()

dev_packages = [
    'bandit',
    'black',
    'codespell',
    'deepdiff',
    'flake8',
    'isort',
    'mako',
    'pre-commit',
    'pydocstyle',
    'pylint>=2.5.0',
    'pytest',
    'pytest-cov',
    'pytest-html',
    'pytest-xdist>=2.0.0',
    'pyupgrade',
]


setup(
    author=metadata['__author__'],
    author_email=metadata['__author_email__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Security',
    ],
    description=metadata['__description__'],
    download_url=metadata['__download_url__'],
    extras_require={'dev': dev_packages, 'develop': dev_packages, 'development': dev_packages},
    include_package_data=True,
    install_requires=[
        'arrow',
        'backports.cached-property; python_version < "3.8.0"',
        'colorama>=0.3.9',
        'future',
        'hvac>=0.3.0',
        'inflect>=0.2.5',
        'jmespath',
        'jsonschema>=2.6.0',
        'lark',
        'paho-mqtt',
        'parsedatetime',
        'pyaes',
        'pydantic',
        'python-dateutil>=2.6.1',
        'pytz',
        'pyyaml',
        'redis>=2.10.6',
        'requests',
        'semantic_version',
        'six>=1.11.0',
        'stdlib-list>=0.6.0',
        'stix2',
        'tinydb',
        'typer',
        'tzlocal',
        'wrapt',
    ],
    license=metadata['__license__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    name=metadata['__package_name__'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'': ['*.json', '*.lark']},
    package_dir={'tcex': 'tcex'},
    project_urls={
        'Documentation': 'https://threatconnect-inc.github.io/tcex/',
        'Source': 'https://github.com/ThreatConnect-Inc/tcex',
    },
    python_requires='>=3.6',
    scripts=[
        'bin/tcex',
    ],
    url=metadata['__url__'],
    version=metadata['__version__'],
    zip_safe=True,
)
