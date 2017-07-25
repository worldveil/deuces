"""
Deuces: A pure Python poker hand evaluation library
"""

from setuptools import setup
import io

setup(
    name='deuces',
    version='0.1',
    description=__doc__,
    long_description=io.open('README.md', encoding="utf-8").read(),
    author='Will Drevo',
    url='https://github.com/worldveil/deuces',
    license='MIT',
    packages=['deuces'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment'
    ]
)