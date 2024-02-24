=====
Usage
=====

Installation
============

Install library into your documentation project from PyPI.

.. code:: console

   pip install rst-package-refs

Integrate Sphinx document
-------------------------

Add bundled extension into your ``conf.py`` of document.

.. code-block:: python
   :caption: conf.py

   extensions = [
       "rst_package_refs.sphinx",
   ]

Write a document
================

You can write text with custom roles in integrated document.

.. tabs::

   .. tab:: reST

      .. code:: rst

         :pypi:`rst-package-refs` provides custom roles to refer for packages of PyPI.

   .. tab:: MyST

      .. code:: md

         {pypi}`rst-package-refs` provides custom roles to refer for packages of PyPI.

This source is rendered like ths on HTML.

  :pypi:`rst-package-refs` provides custom roles to refer for packages of PyPI.
