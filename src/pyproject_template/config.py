import sys
import tomllib

#TODO: 2/2/26-Replace print with log

class Config:
    _CONFIG_PATH='config.toml'

    def __init__(self):
        """The class attribute self._data will be empty if
        the configuration file can not be found. It is up
        to the caller to access the data property and verify
        the dictionary state.
        """
        self._data=dict()
        try:
            with open(self._CONFIG_PATH, 'rb') as cf:
                self._data = tomllib.load(cf)
        except FileNotFoundError:
            print(f'Config file \'{self._CONFIG_PATH}\' not found \
                    \nConfig data could not be initialized')

    @property
    def data(self):
        """This function creates a new dictionary and returns
        it to the caller.
        This means mutations to the returned dictionary will
        not affect the _data class attribute.
        """
        return dict(self._data)
