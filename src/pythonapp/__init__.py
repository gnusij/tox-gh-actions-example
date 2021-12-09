from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

from . import core

__all__ = [
    "core",
]

class PythonApp(object):
    _module = sys.modules[__name__]

    def __dir__(self):
        return __all__

    def __getattr__(self, name):
        if name in dir(self):
            return globals()[name]

sys.modules[__name__] = PythonApp()
