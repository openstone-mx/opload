import os

from fred.version import Version


def get_current_version() -> Version:
    return Version.from_path(name="opload", dirpath=os.path.dirname(__file__))
