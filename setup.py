from setuptools import setup, find_packages

setup(
    name="blog_de_toolkit",
    version="0.1.0",
    description="A Python toolkit for data engineering tasks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "blog_de_toolkit=de_toolkit.data_tools:main",  # Entry point for the CLI
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
