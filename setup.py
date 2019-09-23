"""
-- User: Ashok Kumar Pant (ashokpant@treeleaf.ai)
-- Treeleaf Technologies Pvt. Ltd.
-- Date: 9/18/19
-- Time: 4:17 PM
"""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except IOError as e:
    print(e)

test_requirements = [
]

setup(
    name='deep_sort',
    version='1.0',
    description="deep_sort",
    long_description=readme + '\n',
    author="Ashok Kumar Pant",
    author_email='ashokpant@treeleaf.ai',
    packages=find_packages(include="*"),
    package_dir={},
    package_data={},
    install_requires=requirements,
    zip_safe=False,
    keywords='deep_sort',
    classifiers=[
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
