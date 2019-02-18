#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TcEx App Init."""

import json
import os
from builtins import input

import requests
import colorama as c

from .tcex_bin import TcExBin


class TcExInit(TcExBin):
    """Install required modules for ThreatConnect Job or Playbook App.

    Args:
        _args (namespace): The argparser args Namespace.
    """

    def __init__(self, _args):
        """Initialize Class properties.

        Args:
            _args (namespace): The argparser args Namespace.
        """
        super(TcExInit, self).__init__(_args)

        # properties
        self.base_url = (
            'https://raw.githubusercontent.com/ThreatConnect-Inc/tcex/{}/app_init/'
        ).format(self.args.branch)

    @staticmethod
    def _print_results(file, status):
        """Print the download results.

        Args:
            file (str): The filename.
            status (str): The file download status.
        """

        file_color = c.Fore.GREEN
        status_color = c.Fore.RED
        if status == 'Success':
            status_color = c.Fore.GREEN
        elif status == 'Skipped':
            status_color = c.Fore.YELLOW
        print(
            '{}{!s:<20}{}{!s:<35}{}{!s:<15}{}{!s:<15}'.format(
                c.Fore.CYAN,
                'Downloading:',
                file_color,
                file,
                c.Fore.CYAN,
                'Status:',
                status_color,
                status,
            )
        )

    @staticmethod
    def _confirm_overwrite(filename):
        """Confirm overwrite of template files.

        Make sure the user would like to continue downloading a file which will overwrite a file
        in the current directory.

        Args:
            filename (str): The name of the file to overwrite.

        Returns:
            bool: True if the user specifies a "yes" response.
        """

        message = '{}Would you like to overwrite the contents of {} (y/[n])? '.format(
            c.Fore.MAGENTA, filename
        )
        response = input(message) or 'n'
        response = response.lower()

        if response in ['y', 'yes']:
            return True
        return False

    def check_empty_app_dir(self):
        """Check to see if the directory in which the app is going to be created is empty."""
        if not os.listdir(self.app_path):
            self.handle_error(
                'No app exists in this directory. Try using "tcinit --template '
                '{} --action create" to create an app.'.format(self.args.template)
            )

    def download_file(self, remote_filename, local_filename=None):
        """Download file from github.

        Args:
            remote_filename (str): The name of the file as defined in git repository.
            local_filename (str, optional): Defaults to None. The name of the file as it should be
                be written to local filesystem.
        """
        status = 'Failed'
        if local_filename is None:
            local_filename = remote_filename

        if not self.args.force and os.access(local_filename, os.F_OK):
            if not self._confirm_overwrite(local_filename):
                self._print_results(local_filename, 'Skipped')
                return

        url = '{}{}'.format(self.base_url, remote_filename)
        r = requests.get(url, allow_redirects=True)
        if r.ok:
            open(local_filename, 'wb').write(r.content)
            status = 'Success'
        else:
            self.handle_error('Error requesting: {}'.format(url), False)

        # print download status
        self._print_results(local_filename, status)

    @staticmethod
    def update_install_json():
        """Update the install.json configuration file if exists."""
        if not os.path.isfile('install.json'):
            return

        with open('install.json', 'r') as f:
            install_json = json.load(f)

        if install_json.get('programMain'):
            install_json['programMain'] = 'run'

        # update features
        install_json['features'] = ['aotExecutionEnabled', 'appBuilderCompliant', 'secureParams']

        with open('install.json', 'w') as f:
            json.dump(install_json, f, indent=2, sort_keys=True)

    @staticmethod
    def update_tcex_json():
        """Update the tcex.json configuration file if exists."""
        if not os.path.isfile('tcex.json'):
            return

        with open('tcex.json', 'r') as f:
            tcex_json = json.load(f)

        # display warning on missing app_name field
        if tcex_json.get('package', {}).get('app_name') is None:
            print('{}The tcex.json file is missing the "app_name" field.'.format(c.Fore.MAGENTA))

        # display warning on missing app_version field
        if tcex_json.get('package', {}).get('app_version') is None:
            print('{}The tcex.json file is missing the "app_version" field.'.format(c.Fore.YELLOW))

        # update excludes
        excludes = [
            '.gitignore',
            '.pre-commit-config.yaml',
            'pyproject.toml',
            'setup.cfg',
            'tcex.json',
            '*.install.json',
            'tcex.d',
        ]

        missing_exclude = False
        for exclude in excludes:
            if exclude not in tcex_json.get('package').get('excludes', []):
                missing_exclude = True
                break

        if missing_exclude:
            message = '{}The tcex.json file is missing excludes items. Update ([y]/n)? '.format(
                c.Fore.YELLOW
            )
            response = (input(message) or 'y').lower()

            if response in ['y', 'yes']:
                # get unique list of excludes
                excludes.extend(tcex_json.get('package', {}).get('excludes'))
                tcex_json['package']['excludes'] = sorted(list(set(excludes)))

                with open('tcex.json', 'w') as f:
                    json.dump(tcex_json, f, indent=2, sort_keys=True)
