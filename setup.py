from setuptools import find_packages, setup
import pathlib

curr_path = pathlib.Path(__file__).parent.resolve()

# Get long description from readme file.
long_description = (curr_path/"README.md").read_text(encoding="utf-8")

setup(
    name = "frypto",
    version = "0.1.0",
    description = "Crypto data feature engineering package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abderlahman Elsayed",
    author_email="bedoelsayed785@gmail.com",
    packages=find_packages(where="."),
    install_requires=[  
        "pandas",
        "numpy",
        "scipy",
        "numba"],
)