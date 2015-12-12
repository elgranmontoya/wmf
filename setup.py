from setuptools import setup, find_packages

setup(
    name='wmf',
    packages=find_packages(),
    version='0.1.2',
    description='Tools from the Wikimedia Foundation, such as a pageview API client',
    author='Dan Andreescu',
    author_email='dan.andreescu@gmail.com',
    url='https://github.com/milimetric/wmf',
    download_url='https://github.com/milimetric/wmf/tarball/0.1.1',
    keywords=['wmf', 'wikimedia', 'wikipedia', 'pageview', 'api'],
    install_requires=[
        'requests>=2.4',
    ],
    classifiers=[],
)
