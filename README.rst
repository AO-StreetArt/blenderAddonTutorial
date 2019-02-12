Testable Blender Addons
=======================

This repository contains the source code for the tutorial 'Testable Blender Addons'

Bundling the Addon
------------------

The following command, run from the directory above the repository,
will build a zip file of this addon on a Linux system.  Windows
users can simply zip up the repository folder from the File Explorer.

.. code-block:: bash

   zip -r moveObjectAddon.zip moveObjectAddon/ -x *.git* -x *test.py -x *mock.py -x *.pyc
