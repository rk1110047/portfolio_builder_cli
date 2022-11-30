from setuptools import setup,find_packages,version


setup(
    name='portfoliobuilder',
    packages=find_packages(),
    install_requires=[
        'click',
        'aiohttp',
        'requests'
    ],
    version='0.0.0',
    long_description_content_type="text/markdown",
    entry_points='''    
    [console_scripts]
    portfoliobuilder=portfoliobuilder:portfoliobuilder
    '''

)