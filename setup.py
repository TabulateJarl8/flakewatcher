import setuptools
import os

install_requires = [
	"PyQt5>=5.13",
]

with open('README.md', 'r') as fh:
	long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'flakewatcher', '__version__.py'), 'r') as f:
	exec(f.read(), about)

packages = ['flakewatcher']

setuptools.setup(
	name=about['__title__'],
	version=about['__version__'],
	author=about['__author__'],
	author_email=about["__author_email__"],
	description=about["__description__"],
	long_description=long_description,
	long_description_content_type="text/markdown",
	url=about["__url__"],
	install_requires=install_requires,
	packages=packages,
	package_dir={'flakewatcher': 'flakewatcher'},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Natural Language :: English",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
