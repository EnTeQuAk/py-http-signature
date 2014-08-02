from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()
with open('CHANGES.rst') as file:
    long_description += '\n\n' + file.read()

setup(
    name='http_signature',
    version='0.2.0',
    description='Simple secure signing for HTTP requests using http-signature',
    long_description=long_description,
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 3 - Alpha',
    ],
    keywords='http,cryptography,web,joyent',
    author='Adam T. Lindsay',
    author_email='a.lindsay+github@gmail.com',
    url='https://github.com/atl/py-http-signature',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['pycrypto', 'six']
)
