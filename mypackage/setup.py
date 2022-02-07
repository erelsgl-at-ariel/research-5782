import setuptools, pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
print("\nREADME", README, "\n")
REQUIRES = (HERE / "requirements.txt").read_text().strip().split("\n")
REQUIRES = [lin.strip() for lin in REQUIRES]
print("\nREQUIRES", REQUIRES, "\n")

__version__ = "0.1.0"

setuptools.setup(
    name="mypackage",
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=REQUIRES,
    author="Erel Segal-Halevi",
    author_email="erelsgl@gmail.com",
    description="Example PyPI Package",
    keywords="example, pypi, package",
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Documentation": "",
        "Bug Reports": "",
        "Source Code": "",
    },
    python_requires=">=3.8",
    include_package_data=True,
)

# Build:
#   [delete old folders: build, dist, test_env]
#   python setup.py sdist bdist_wheel


# Publish to test PyPI:
#   twine upload --repository testpypi dist/*

# Publish to real PyPI:
#   twine upload --repository pypi dist/*


# Test in a virtual environment:
#    cd ..
#    virtualenv test_env
#    test_env\Scripts\activate
#    pip install numpy
#    pip install -i https://test.pypi.org/simple/ example-pypi-package-5782
#    pytest test_env\Lib\site-packages\examplepy
