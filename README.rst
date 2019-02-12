Testable Blender Addons
=======================

This repository contains the source code for the tutorial 'Testable Blender Addons'

Running Unit Tests
------------------

Unit tests can be run with the below command, from the 'addon_logic' folder:

.. code-block:: bash

   python3 -m test.move_object_test

Bundling the Addon
------------------

The following command, run from the directory above the repository,
will build a zip file of this addon on a Linux system.  Windows
users can simply zip up the repository folder from the File Explorer.

.. code-block:: bash

   zip -r moveObjectAddon.zip moveObjectAddon/ -x *.git* -x *test.py -x *mock.py -x *.pyc
