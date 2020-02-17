from setuptools import setup

setup(
    name="awssecrets",
    version="0.1",
    entry_points={"console_scripts": ["awssecrets = awssecrets.main:main"]},
    packages=["awssecrets"],
    install_requires=["boto3 == 1.12.0"],
    zip_safe=True,
)
