from setuptools import setup, find_packages

setup(
    name='MetricWriterPy',
    version='0.1.1',
    description='A simple Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NicolasEurotech/MetricWriterPy.git',  # Replace with the URL of your GitHub repository
    author='Your Name',
    author_email='your@email.com',
    license='MIT',  # Choose an appropriate license for your library
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10.6',
    ],
    keywords='example library',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],  # Add any dependencies your library requires
)