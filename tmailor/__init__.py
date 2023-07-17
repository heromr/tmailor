__title__ = 'tmailor'
__author__ = 'heromr'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023 HeroMR'
__version__ = '0.0.12'
__description__ = 'A temporary email address that provides email addresses without registration, used to receive incoming emails without disclosing your actual email.'


from .client import Client

from requests import get
from colorama import Fore, Style

latestVersion = get("https://pypi.org/pypi/tmailor/json").json()["info"]["version"]

if __version__ != latestVersion:
    print(f"{Fore.RED}WARNING:{Style.RESET_ALL} You are using an outdated version of tmailor ({__version__}). The latest version is {latestVersion}.")
