# Try using setuptools first, if it's installed
try:
    from setuptools import setup
except:
    from distutils.core import setup

# define all packages for distribution
packages = [
    'npfuncs',
]

setup(name='npfuncs',
      version='0.1',
      description='',
      author='Zach Sailer',
      author_email='zachsailer@gmail.com',
      url='https://github.com/Zsailer/npfuncs',
      packages=packages,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
      zip_safe=False)
