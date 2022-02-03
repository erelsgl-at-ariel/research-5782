import setuptools, pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
REQUIRES = (HERE / "requirements.txt").read_text().strip().split("\n")
REQUIRES = [lin.strip() for lin in REQUIRES]
print("REQUIRES", REQUIRES)

from examplepy import __version__ 

setuptools.setup(
    name='example_pypi_package_5782',
    version=__version__,

    # packages=setuptools.find_packages(exclude=["tests"]),
    packages=setuptools.find_packages(),
    install_requires=REQUIRES,

    author='Tom Chen',
    author_email='tomchen.org@gmail.com',
    description='Example PyPI Package',
    keywords='example, pypi, package',
    license="MIT",

    long_description=README,
    long_description_content_type='text/markdown',

    url='https://github.com/tomchen/example_pypi_package',
    project_urls={
        'Documentation': 'https://github.com/tomchen/example_pypi_package',
        'Bug Reports':
        'https://github.com/tomchen/example_pypi_package/issues',
        'Source Code': 'https://github.com/tomchen/example_pypi_package',
    },

    python_requires='>=3.6',
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 7 - Inactive',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    include_package_data= True,
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
