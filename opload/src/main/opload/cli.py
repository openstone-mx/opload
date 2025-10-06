from typing import Optional

from fred.cli.interface import AbstractCLI
from fred.cli.main import CLI as FredCLI

from opload.utils import get_current_version


class CLI(AbstractCLI):

    @property
    def fred(self) -> FredCLI:
        return FredCLI.default_config()

    def version(self) -> str:
        return get_current_version().value
    
    def serve(self, classname: Optional[str] = None, classpath: Optional[str] = None, **kwargs):
        return self.fred.serve(
            classpath=classpath or "opload.router.catalog",
            classname=classname or "RouterCatalog",
            **kwargs
        )