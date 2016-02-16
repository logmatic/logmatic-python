from distutils.core import setup

setup(
    name='logmatic-python',
    version='0.0.1',
    author='Logmatic.io support team',
    author_email='support@logmatic.io',
    package_dir = {'': 'src'},
    packages = find_packages("src", exclude="tests"),
    scripts=[],
    url='https://github.com/logmatic/logmatic-python',
    license='MIT',
    description='Python plugin to send logs to Logmatic.io',
    long_description=open('README.md').read(),
    install_requires=[
        "logging.handlers",
        "python-json-logger"
    ],
)
