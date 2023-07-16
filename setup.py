from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

VERSION = "0.0.10"
DESCRIPTION = "A temporary email address is: a library that provides email addresses without registration, used to receive incoming emails without disclosing your actual email."

setup(
    name="tmailor",
    version=VERSION,
    description=DESCRIPTION,
    author="HeroMR",
    author_email="mrhero4006@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/heromr/tmailor",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "tmailor", "temp mail", "disposable email", "temp mailbox", "fake email"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)