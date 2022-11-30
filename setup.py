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
    entry_points='''    
    [console_scripts]
    portfolio_builder_cli=portfoliobuilder:portfoliobuilder
    '''

)