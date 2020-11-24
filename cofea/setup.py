from setuptools import setup

setup(name='cofea',
      version='0.1',
      description="A CoFEA Initiative project",
      long_description="",
      python_requires=">=3.6",
      author='Slawomir Polanski',
      author_email='polanski.slawomir@gmail.com',
      license='TODO',
      packages=['cofea', 'docs'],
      zip_safe=False,
      install_requires=[
          'jinja2',
          'sphinx',
          'pydata-sphinx-theme~=0.4.1',
          'myst-nb',
          'sphinx-copybutton',
          'sphinx-togglebutton',
          'sphinxcontrib-bibtex',
          'sphinx-thebe',
          'ablog', ],
      )