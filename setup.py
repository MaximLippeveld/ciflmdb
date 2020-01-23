import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ciflmdb",
    version="1.0.0",
    author="Maxim Lippeveld",
    author_email="lippeveld.maxim@gmail.com",
    description="Python package for reading LMDB file created from CIF with cifconvert (see https://github.com/MaximLippeveld/cifconvert).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaximLippeveld/ciflmdb",
    packages=setuptools.find_packages(),
    python_requires=">3.6.1",
    install_requires=open("requirements.txt", "r").read().split("\n"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
