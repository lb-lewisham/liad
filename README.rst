liad
====

Install
-------

.. code-block:: sh
   :linenos:

    pip install git+https://github.com/lb-lewisham/liad.git

* Free software: GNU General Public License v3

Example use
-----------

.. code-block:: python

    from liad import colab

    # Guess if we are in a colab notebook
    if colab.in_colab():
        from google.colab import drive
        drive.mount("/content/gdrive")
        project_dir = "/content/gdrive/PROJECTPATH"
    else:
        project_dir = "/Volumes/GoogleDrive/PROJECTPATH"
    

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
