import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipenv-pex",
    version="0.1",
    author="Maor Kadosh",
    description="Generate Python executable files via PEX using info from Pipfile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/it-is-wednesday/pipenv-pex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)