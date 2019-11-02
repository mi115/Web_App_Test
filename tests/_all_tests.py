import sys
import os

container_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
))
sys.path.insert(0, container_folder)

# noinspection PyUnresolvedReferences
from tests.account_tests import *
# noinspection PyUnresolvedReferences
from tests.home_tests import *
# noinspection PyUnresolvedReferences
from tests.package_tests import *
# noinspection PyUnresolvedReferences
from tests.sitemap_tests import *
