from setuptools import setup,find_packages


with open('akData/version.py') as fin: exec(fin)

setup(
    name='akData',
    version=__version__,

    packages=find_packages(),
    
    # PyPI MetaData
    author='Adam Kerz',
    author_email='adam@kerz.id.au',
    description='Data manipulation - formatting, parsing, validating and converting',
    license='BSD 3-Clause',
    keywords='data',
    url='',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ),
)
