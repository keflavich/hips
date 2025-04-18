# this contains imports plugins that configure py.test for astropy tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.

import os
import pytest
try:
    # For astropy 4.0 and later
    from pytest_astropy_header.display import PYTEST_HEADER_MODULES, TESTED_VERSIONS
except ImportError:
    try:
        # For astropy 3.0 and later
        from astropy.tests.plugins.display import PYTEST_HEADER_MODULES, TESTED_VERSIONS
    except ImportError:
        # For astropy < 3.0
        try:
            from astropy.tests.pytest_plugins import PYTEST_HEADER_MODULES, TESTED_VERSIONS
        except ImportError:
            PYTEST_HEADER_MODULES = {}
            TESTED_VERSIONS = {}

## Uncomment the following line to treat all DeprecationWarnings as
## exceptions
# enable_deprecations_as_exceptions()

PYTEST_HEADER_MODULES.clear()
PYTEST_HEADER_MODULES.update([
    ('numpy', 'numpy'),
    ('Pillow', 'PIL'),
    ('scikit-image', 'skimage'),
    ('Astropy', 'astropy'),
    ('astropy-healpix', 'astropy_healpix'),
    ('aiohttp', 'aiohttp'),
    ('reproject', 'reproject'),
    ('matplotlib', 'matplotlib'),
])


# This is to figure out the affiliated package version, rather than
# using Astropy's
try:
    from .version import version
except ImportError:
    version = 'dev'

packagename = os.path.basename(os.path.dirname(__file__))
TESTED_VERSIONS[packagename] = version
