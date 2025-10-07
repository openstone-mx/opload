from fred.version import Version

from opload.utils import get_current_version


def test_get_current_version():
    version = get_current_version()
    assert isinstance(version, Version)
    assert isinstance(version.major, int)
    assert isinstance(version.minor, int)
    assert isinstance(version.patch, int)
