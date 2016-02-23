from distutils.core import setup

setup(
    name='logmatic-python',
    version='0.0.8',
    author='Logmatic.io support team',
    author_email='support@logmatic.io',
    packages = ['logmatic'],
    scripts=[],
    url='https://github.com/logmatic/logmatic-python',
    license='MIT',
    long_description=open('README.rst').read(),
    description='Python plugin to send logs to Logmatic.io',
    install_requires = ['python-json-logger']
)
