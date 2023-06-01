from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pyroccs_tracking_system/__init__.py
from pyroccs_tracking_system import __version__ as version

setup(
	name="pyroccs_tracking_system",
	version=version,
	description="PyroCCS Tracking System",
	author="Deepak Kumar",
	author_email="deepakkumar@8848digital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
