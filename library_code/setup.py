import setuptools
from glob import glob

# Pull project description from README
with open("README.md") as f:
    README = f.read()

# Increment according to semantic versioning, google if necessary
version = "0.0.0"

#
with open('requirements.txt', 'r') as req_file:
    requirements = [line.strip() for line in req_file]

setuptools.setup(
    author="Carl Schaffer",
    author_email="cfmschaffer@hotmail.de",
    name="library_code",
    license="MIT",
    description="library code for ebook scraping",
    version=version,
    long_description=README,
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    # Adds executable scripts to the installer, they can be executed directly from shell in any environment where the package is installed.
    scripts=glob("bin/*"),
    # Dependencies are listed in 'requirements.txt'
    install_requires=requirements,
    #Update Classifiers as you see fit. If in doubt, leave as is and only update the license
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
)
