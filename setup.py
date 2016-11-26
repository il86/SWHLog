from setuptools import setup

exec(open("./swhlog/version.py").read()) # pull version from this file

setup(
    name='swhlog',
    version=__version__,
    author='Scott W Harden',
    author_email='SWHarden@gmail.com',
    packages=['swhlog'],
    url='https://github.com/swharden/swhlog',
    license='MIT License',
    platforms='any',
    description='extremely simple logging/debugging package. See github for demos.',
    long_description=open("README.md").readlines()[1],
    keywords="""logging debugging""",
    install_requires=[],    
    classifiers=[
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
       'Intended Audience :: Developers',
    ]
)