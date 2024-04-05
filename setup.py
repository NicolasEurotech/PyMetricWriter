from setuptools import setup, find_packages

setup(
    name='MetricWriterPy',
    version='0.1.1',
    description='A metrci writer for prometheus in python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NicolasEurotech/MetricWriterPy.git',  # Replace with the URL of your GitHub repository
    author='Nicolas Marcuzzi',
    author_email='marcuzzi.nicolas.95@gmail.com',
    license='MIT',  
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10.6',
    ],
    keywords='metric writer prometheus',
    packages=find_packages(
        include=['MetricWriterPy', 'MetricWriterPy.*']
    ),
    python_requires='>=3.6',
    install_requires=[]
)