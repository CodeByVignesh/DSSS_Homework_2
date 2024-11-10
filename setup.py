from setuptools import setup, find_packages

setup(
    name="mathematics_quiz",           # Package name
    version="0.1.0",                   # Version of your package
    description="A simple mathematical quiz game",  # Short description
    long_description=open("README.md").read(),  # Long description from the README file
    long_description_content_type="text/markdown",  # Format for the long description
    author="Vigneshkumar Selvaraj",   # Your name
    author_email="vigneshkumar.selvaraj27@gmail.com",  # Your email
    url="https://github.com/CodeByVignesh/DSSS_Homework_2.git",  # URL to your project (e.g., GitHub)
    license="Apache-2.0",              # License type
    packages=find_packages(where="mathematics_quiz"),  # Find packages in the mathematics_quiz directory
    package_dir={"": "mathematics_quiz"},  # Tell setuptools where to look for the package
    install_requires=[],               # List any dependencies here, if required
    classifiers=[
        "Programming Language :: Python :: 3",  # Python version compatibility
        "License :: OSI Approved :: Apache Software License",  # License information
        "Operating System :: OS Independent",  # OS compatibility
    ],
    python_requires=">=3.7",            # Minimum Python version required
)
