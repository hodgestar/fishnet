from setuptools import setup, find_packages

setup(
    name="fishnet",
    version="0.0.1",
    url='http://github.com/hodgestar/fishnet',
    license='MIT',
    description=(
        "A thing with lots of holes for trawling through data scattered over"
        " multiple machines."),
    long_description=open('README.md', 'r').read(),
    author='Simon Cross',
    author_email='hodgestar@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyYAML',
        'execnet',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
