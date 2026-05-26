import os as _os
import sys as _sys

# dinov2, clipeval, and prompt use bare absolute imports (e.g. `from dinov2.layers import ...`),
# so this package's own directory must be on sys.path.
_pkg_dir = _os.path.dirname(_os.path.abspath(__file__))
if _pkg_dir not in _sys.path:
    _sys.path.insert(0, _pkg_dir)

from . import clipeval
from . import dinov2
from . import prompt
from .models_clip import *
