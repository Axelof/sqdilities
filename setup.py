from setuptools import setup, find_packages

setup(
    name="sqdilities",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["aiohttp[speedups]==3.10.10"],
    extras_require={
        'geo': ["maxminddb==2.6.2"],
    },
    author="axelof",
    author_email="me@sqd.su",
    description="Набор инструментов для проектов Squad'a.",
    package_data={},
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/axelof/sqdilities",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'sqdilities=sqdilities.cli:main'
        ],
    }
)
