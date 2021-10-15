from setuptools import setup, find_packages

version = '0.3.dev0'

setup(name='ipplf.db.pgsql',
      version=version,
      description="DB postgresql connexion",
      classifiers=[],  # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='postgresql ipplf',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='http://svn.affinitic.be/plone/ipplf/ipplf.db.pgsql',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ipplf', 'ipplf.db'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'sqlalchemy',
        'z3c.autoinclude',
        'z3c.sqlalchemy',
        'affinitic.pwmanager'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
