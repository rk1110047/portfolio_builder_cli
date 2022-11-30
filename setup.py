from setuptools import setup,find_packages,version

setup(
    name='portfoliobuilder',
    packages=['src']+['src.'+ pkg for pkg in find_packages('src')],
    author_email="ravinder.kumar@researchandranking.com",
    author="ravinder",
    install_requires=[
        'click',
        'aiohttp',
        'requests'
    ],

    version='0.0.6',
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts":["portfoliobuilder=src.portfoliobuilder:portfoliobuilder"]
    },
    zip_safe=True,
)