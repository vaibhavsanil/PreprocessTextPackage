import setuptools

with open('README.md','r') as file:
    long_description = file.read()

setuptools.setup(
    name= 'preprocess_vaibhav',
    version = "0.0.1",
    author = "Laxmi Kant",
    author_email = "udemy@kgptalkie.com",
    Long_description= long_description,
    Long_desription_content_type = "text/markdown"
    packages = setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 3',
    'License :: OSI Aproved :: MIT License',
    "Operating System :: OS Independent"
    ],
    python_requires = '>=3.5'

)