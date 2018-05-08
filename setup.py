from setuptools import setup

setup(name='receiptor',
      version='0.1',
      description="This the a reminder tool for people who don't want to forget to drink water!",
      url='http://github.com/assli100/receiptor',
      author='Matan Assli',
      author_email='matanasslizada@gmail.com',
      license='GPL',
      packages=['receiptor'],
      zip_safe=False, install_requires=['telegram', 'beautifulsoup4', 'requests'])
