from setuptools import setup

setup(name='CoFEA',
      version='0.1',
      description="mesh converter which is a part of the CoFEA Initiative project",
      long_description="",
      python_requires=">=3.6",
      author='Slawomir Polanski',
      author_email='polanski.slawomir@gmail.com',
      license='TODO',
      packages=['meshpresso', 'docs'],
      zip_safe=False,
      install_requires=[
          'jinja2',
          'pyyaml',
          'docutils>=0.15',
          'sphinx>=2.0',
          'click',
          'pydata-sphinx-theme~=0.4.1',
          'beautifulsoup4',
          'importlib-resources~=3.0.0; python_version < "3.7"',
          'myst-nb',
          'sphinx-copybutton',
          'sphinx-togglebutton',
          'sphinxcontrib-bibtex',
          'sphinx-thebe',
          'ablog',
          'nbsphinx',
          'nbconvert~=5.6',
          'ipygany',
          'ipywidgets<8,>=7.0.0',
          'vtk',
          'pyvista',
          'meshpy',
          'jupyter-sphinx',
          'pygments==2.6.1',
          'sphinx-book-theme', ],
      )
