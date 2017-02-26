from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='sparkapi',
      version='0.1',
      description='A Nice Python API to CISCO spark',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
      ],
      keywords='CISCO Spark Python API',
      long_description=readme(),
      url='https://github.com/Abdellbar/sparkapi',
      download_url = 'https://github.com/Abdellbar/sparkapi/tarball/0.1',
      author='Abdelbar Aglagane',
      author_email='abdellbar@gmail.com',
      license='Apache License 2.0',
      packages=['sparkapi'],
      install_requires=[
          'unirest',
          'json'
      ],
      include_package_data=True,
      zip_safe=False)