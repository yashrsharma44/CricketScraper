from setuptools import setup, find_packages

setup(
    name='CricketScraper',
    version='0.1',
    description = 'CLI tool for scraping cricket scores',
    author = 'Yash Sharma',
    author_email = 'yashrsharma44@gmail.com',
    #py_modules=['CricketScraper'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'bs4',
        'requests'
    ],
    entry_points='''
       [console_scripts]
       getlist=src.display:main
       getSummary=src.summary:main
       getScore=src.scorecard:main
    ''',
)