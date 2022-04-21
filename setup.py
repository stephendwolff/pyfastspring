import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyfastspring',
    version="0.0.1",
    author='Artlogic Media Limited',
    author_email='support@artlogic.net',
    description='A module for working with the FastSpring orders and subscriptopns API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/stephendwolff/pyfastspring',
    project_urls={
        "Bug Tracker": "https://github.com/stephendwolff/pyfastspring/issues",
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    package_dir={"": ""},
    packages=setuptools.find_packages(where=""),
    python_requires=">=3.6",
)
