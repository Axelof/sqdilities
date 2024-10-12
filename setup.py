from setuptools import setup, find_packages

setup(
    name="sqdilities",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["aiohttp[speedups]==3.10.10"],
    author="axelof",
    author_email="me@sqd.su",
    description="Набор инструментов для проектов Squad'a.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/axelof/sqdilities",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
