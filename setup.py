from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='LensMotionMania',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    description='Dip package for images and videos ',
    author='Mahsa Sanaei',
    author_email='mahsasanaei.n@gmail.com',
    url='https://github.com/snmahsa/ImageToolkit',
    keywords =['Image Processing','Machine Learning','Deep Learning','Noises','Filters','Image']
 
    )
