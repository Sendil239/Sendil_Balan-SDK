from setuptools import setup, find_packages

setup(
    name='psbSDK',
    version='1.0.7',
    description='An SDK for interacting with the Movie API endpoint',
    url='https://github.com/Sendil239/Sendil_Balan-SDK',
    author='Sendil Balan Palanivel',
    author_email='sendilbalan@gmail.com',
    packages=['psbSDK'],
    install_requires=[
        'requests>=2.26.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)