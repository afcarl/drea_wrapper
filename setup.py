#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Eric Hendricks',
 'author_email': 'eric.hendricks@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO component wrapper for DREA',
 'download_url': '',
 'entry_points': '[openmdao.component]\ndrea_wrapper.DREA.DREA=drea_wrapper.DREA:DREA\n\n[openmdao.container]\ndrea_wrapper.geometry.Geometry=drea_wrapper.geometry:Geometry\ndrea_wrapper.stream.Stream=drea_wrapper.stream:Stream\ndrea_wrapper.MEflows.MEflows=drea_wrapper.MEflows:MEflows\ndrea_wrapper.DREA.DREA=drea_wrapper.DREA:DREA',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kenneth Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'drea_wrapper',
 'package_data': {'drea_wrapper': ['sphinx_build/html/.buildinfo',
                                   'sphinx_build/html/genindex.html',
                                   'sphinx_build/html/index.html',
                                   'sphinx_build/html/objects.inv',
                                   'sphinx_build/html/pkgdocs.html',
                                   'sphinx_build/html/py-modindex.html',
                                   'sphinx_build/html/search.html',
                                   'sphinx_build/html/searchindex.js',
                                   'sphinx_build/html/srcdocs.html',
                                   'sphinx_build/html/usage.html',
                                   'sphinx_build/html/_modules/index.html',
                                   'sphinx_build/html/_modules/drea_wrapper/DREA.html',
                                   'sphinx_build/html/_modules/drea_wrapper/geometry.html',
                                   'sphinx_build/html/_modules/drea_wrapper/MEflows.html',
                                   'sphinx_build/html/_modules/drea_wrapper/stream.html',
                                   'sphinx_build/html/_modules/drea_wrapper/test/test_drea_wrapper.html',
                                   'sphinx_build/html/_sources/index.txt',
                                   'sphinx_build/html/_sources/pkgdocs.txt',
                                   'sphinx_build/html/_sources/srcdocs.txt',
                                   'sphinx_build/html/_sources/usage.txt',
                                   'sphinx_build/html/_static/ajax-loader.gif',
                                   'sphinx_build/html/_static/basic.css',
                                   'sphinx_build/html/_static/comment-bright.png',
                                   'sphinx_build/html/_static/comment-close.png',
                                   'sphinx_build/html/_static/comment.png',
                                   'sphinx_build/html/_static/default.css',
                                   'sphinx_build/html/_static/doctools.js',
                                   'sphinx_build/html/_static/down-pressed.png',
                                   'sphinx_build/html/_static/down.png',
                                   'sphinx_build/html/_static/file.png',
                                   'sphinx_build/html/_static/jquery.js',
                                   'sphinx_build/html/_static/minus.png',
                                   'sphinx_build/html/_static/plus.png',
                                   'sphinx_build/html/_static/pygments.css',
                                   'sphinx_build/html/_static/searchtools.js',
                                   'sphinx_build/html/_static/sidebar.js',
                                   'sphinx_build/html/_static/underscore.js',
                                   'sphinx_build/html/_static/up-pressed.png',
                                   'sphinx_build/html/_static/up.png',
                                   'sphinx_build/html/_static/websupport.js',
                                   'test/__init__.py',
                                   'test/base_control.in',
                                   'test/base_drea.dump',
                                   'test/base_ejectd.out',
                                   'test/base_expnd.in',
                                   'test/base_flocond.in',
                                   'test/base_hwall.in',
                                   'test/base_zrdmix.in',
                                   'test/test_drea_wrapper.py']},
 'package_dir': {'': 'src'},
 'packages': ['drea_wrapper', 'drea_wrapper.test'],
 'url': 'https://github.com/OpenMDAO-Plugins/drea_wrapper',
 'version': '0.2.1',
 'zip_safe': False}


setup(**kwargs)

