from setuptools import setup,find_packages,version


setup(
    name='portfolio_builder_cli',
    packages=find_packages(),
    author_email="ravinder.kumar@researchandranking.com",
    author="ravinder",
    install_requires=[
        'click',
        'aiohttp',
        'requests'
    ],

    version='0.0.2',
    long_description_content_type="text/markdown",
    data_files=['portfoliobuilder.py'],
    entry_points='''    
    [console_scripts]
    portfoliobuilder=data.portfoliobuilder:portfoliobuilder
    '''

)