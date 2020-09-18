import setuptools
import os

# Change to the setup.py directory to read files relative to it.
cwd = os.getcwd()
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="flask-hello-world",
    version=1.0,
    author="Teqniqly",
    author_email="farooq@teqniqly.com",
    description="A Hello World Flask app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_namespace_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["Flask==1.1.2",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

# Pop back to the original directory.
os.chdir(cwd)
