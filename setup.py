"""
Deuces: A pure Python poker hand evaluation library
"""

from setuptools import setup

setup(
    name='deuces',
    version='0.2.1',
    description=__doc__,
    long_description=open('README.md').read(),
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
    ],
    #
    # https://docs.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
    #
    setup_requires=['pytest-runner'],
    tests_require=['mock', 'pytest', 'pytest-cov']
)
