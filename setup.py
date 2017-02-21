from setuptools import find_packages, setup


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()


setup(
    name='dollars',
    version='0.1',
    description='Converts everything to dollars using up to date rates for '
                'free',
    url='http://github.com/aerupt/dollars',
    author='Lasse Schuirmann',
    author_email='lasse.schuirmann@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=required,
)
