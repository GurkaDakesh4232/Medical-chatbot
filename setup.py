from setuptools import find_packages, setup

setup(
    name='generative_ai_project',  # Changed to remove spaces
    version='0.0.0',
    author='Bappy Ahmed',
    author_email='entbappy73@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add any dependencies here if needed
    ],
)
