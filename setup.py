from setuptools import setup, find_packages

setup(
    name="stockbot",  # Your package name
    version="0.1",
    packages=find_packages(),  # Automatically find subpackages
    install_requires=[
        "requests",
        "pandas",
        "python-dotenv",
        "pytest"
    ],
    include_package_data=True,
)