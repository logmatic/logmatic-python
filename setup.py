from distutils.core import setup

setup(
    name='logmatic-python',
    version='0.1.7',
    author='Logmatic.io support team',
    author_email='support@logmatic.io',
    packages = ['logmatic'],
    scripts=[],
    url='https://github.com/logmatic/logmatic-python',
    download_url = 'https://github.com/logmatic/logmatic-python/tarball/0.1.6',
    license='MIT',
    long_description=open('README.rst').read(),
    description='Python plugin to send logs to Logmatic.io',
    install_requires = ['python-json-logger'],
    keywords = ['logmatic']
)
