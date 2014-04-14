# -*- coding: utf-8 -*-
'''
The CSV output module converts the return data into CSV.
'''

# Import python libs
import csv
import logging
from StringIO import StringIO

log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'csv'


class CSVOutputGenerator(object):
    """
    This class creates CSV output that will be displayed in the CLI output of a salt module command.
    """

    def __init__(self, data):
        self._data = data
        self._output = None

        self._create_csv()

    def _create_headers(self):
        """
        Sets up default headers and adds headers according to what is found in the data to be output.
        """
        default_headers = ['host', 'output']
        return default_headers

    def _create_csv(self):
        """
        Creates a csv object using StringIO to act like a file
        """
        file = StringIO()
        output = csv.writer(file)

        output.writerow(self._create_headers())

        file.seek(0)

        self._output = file

    def get_output(self):
        for line in csv.reader(self._output):
            yield line


def __virtual__():
    '''
    Rename to csv
    '''
    return __virtualname__


def output(data):
    '''
    Print the output data in CSV
    '''
    return '\n'.join([','.join(line) for line in CSVOutputGenerator(data).get_output()])
