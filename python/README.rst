========
fastdiff
========


.. image:: https://img.shields.io/pypi/v/fastdiff.svg
        :target: https://pypi.python.org/pypi/fastdiff

.. image:: https://img.shields.io/travis/syrusakbary/fastdiff.svg
        :target: https://travis-ci.org/syrusakbary/fastdiff

.. image:: https://readthedocs.org/projects/fastdiff/badge/?version=latest
        :target: https://fastdiff.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/syrusakbary/fastdiff/shield.svg
     :target: https://pyup.io/repos/github/syrusakbary/fastdiff/
     :alt: Updates



A fast/native implementation of diff algorithms using WebAssembly and Wasmer_.

* Free software: MIT license


Features
--------

* Uses WebAssembly to achieve 75x speedup in the compare algorithm
* Compatible with any platform


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Wasmer: https://pypi.org/project/wasmer/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
