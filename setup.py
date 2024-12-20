from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyadbkit",
    version="0.1.0",
    author="PyADBKit Contributors",
    author_email="hanxd3011@gmail.com",
    description="A Python library for interacting with Android devices using ADB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pyadbkit",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "asyncio",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio",
            "flake8",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "pyadbkit=pyadbkit.cli:main",
        ],
    },
)
