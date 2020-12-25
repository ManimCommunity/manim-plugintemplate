Plugin Template
===============
Plugins are features that extend Manim's core functionality. This is a
template project repository that demonstrates how you can create and upload a
manim plugin to PyPI using a PEP 517 compliant build system, `Poetry
<https://python-poetry.org>`_. Feel free to copy the template repository on
GitHub so you can generate a project with the same directory structure,
branches, and files.

Poetry is **NOT** required to create plugins, but is recommended because it
provides build isolation and ensures users can reliably install your plugin
without falling into dependency hell. You may use another build system (e.g.
Flit, Setuptools, Pipenv, etc...) if you wish. 

Creating Plugins
----------------
The only requirement of your preferred build system is that it specifies the
``manim.plugins`` `entry point
<https://packaging.python.org/specifications/entry-points/>`_.

.. note:: 

    The plugin naming convention is to add the prefix ``manim-``. This allows
    users to easily search for plugins on organizations like PyPi, but it is
    not required.

Installing Poetry
~~~~~~~~~~~~~~~~~
Poetry can be installed on Windows, MacOS and Linux. Please visit the
official poetry website for `installation instructions
<https://python-poetry.org/docs/#installation>`_. You may want to see the
official documentation for a list of all `available commands
<https://python-poetry.org/docs/cli/>`_.


Setting Up Your Plugin Directory Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a Python project suitable for poetry, run: 

.. code-block:: bash

	poetry new --src manim-YourPluginName 

.. note:: 

    ``--src`` is both optional and recomended in order to create a src
    directory where all of your plugin code should live.

This will create the following project structure:
:: 

    manim-YourPluginName
    ├── pyproject.toml
    ├── README.rst
    ├── src
    │   └── manim_yourpluginname
    │       └── __init__.py
    └── tests
        ├── __init__.py
        └── test_manim_yourpluginname.py 

If you have already extended manim's functionality, you can instead run:

.. code-block:: bash

    cd path/to/plugin
    poetry init

This will prompt you for basic information regarding your plugin and help
create and populate a ``pyproject.toml`` similar to the one in this template;
however, you may wish to update your project directory structure similarly.

See the official documentation for more information on the `init command
<https://python-poetry.org/docs/cli/#init>`_.

From now on, when working on your plugin, ensure you are using the virtual
environment by running the following at the root of your project:

.. code-block:: bash

    poetry shell 

Updating Pyproject.toml
~~~~~~~~~~~~~~~~~~~~~~~
The ``pyproject.toml`` file is used by Poetry and other build systems to
manage and configure your project. Manim uses the package's entry point
metadata to discover available plugins. The entry point group,
``"manim.plugins"``, is **REQUIRED** and can be `specified as follows
<https://python-poetry.org/docs/pyproject/#plugins>`_:

.. code-block:: toml

    [tool.poetry.plugins."manim.plugins"]
    "manim_yourpluginname" = "module:object.attr"

.. note::

    The left hand side represents the entry point name which should be unique
    among other plugin names. This is the internal name Manim will use to
    identify and handle plugins.

    The right hand side should reference a python object (i.e. module, class,
    function, method, etc...) and will be the first code run in your plugin.
    In the case of this template repository, the package name is used which
    Python interprets as the package's ``__init__.py`` module.

    See the python packaging `documentation
    <https://packaging.python.org/specifications/entry-points/>`_ for more
    information on entry points.

Testing Your Plugin Locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    poetry install

This command will read the ``pyproject.toml``, install the dependencies of
your plugin, and create a ``poetry.lock`` file to ensure everyone using your
plugin gets the same version of dependencies. It is important that your
dependencies are properly annotated with a version constraint (e.g.
``manim:^0.1.1``, ``numpy:*``, etc...). Equally important to the dependencies
specified here is that they do not directly conflict with `Manim's
<https://github.com/ManimCommunity/manim/blob/master/pyproject.toml>`_. If
you want to update the dependencies specified in ``pyproject.toml``, use:

.. code-block:: bash

    poetry update

See the official documentation for more information on `versioning
<https://python-poetry.org/docs/dependency-specification/>`_ or the `install
command <https://python-poetry.org/docs/cli/#install>`_. 


Poetry allows for dependencies that are strictly for project developers.
These are not installed by users. To add them to your project, update the
``pyproject.toml`` file with the section followed by the dependencies:

.. code::toml

    [tool.poetry.dev-dependencies]
    pytest = "*"
    pylint = "*"

The ``pytest`` package is a functional testing framework which you can use to
run the test within the ``manim-YourPluginName/tests`` directory. You should
create files which test the behavior and functionality of your plugin here.
Test first development is a good practice to ensure your code behaves as
intended before packaging and shipping your code publicly. Additionally, you
can create Manimations that depend on your plugin which is another great way
to ensure functionality.

Uploading Your Project
----------------------

By default, poetry is set to register the package/plugin to PyPI. You'll need
to register an account there to upload/update your plugin. As soon as your
plugin is useful locally, run the following:

.. code-block:: bash

    poetry publish --build

This will prompt you for your PyPI username and password; however, it is
recommended to use a project PyPI API token with the username ``__token__``
instead.

Your project should now be available on PyPI for users to install via ``pip
install manim-YourPluginName`` and usable within their respective
environments. If instead you would like to upload to Test PyPI, you can run:

.. code-block:: bash

    poetry config repositories.testpypi https://test.pypi.org/simple/
    poetry publish -r testpypi --build

See the official documentation for more information on the `publish command
<https://python-poetry.org/docs/cli/#publish>`_.

If you are interested in CI/CD pipelines and using GitHub Actions to
automatically publish releases to your PyPI project, you can setup a PyPI API
Token, or PyPI Test API Token for your project. Then on your GitHub
repository you can setup a secret under the repository's settings, followed
by the appropriate GitHub Action.

See the official Python documentation on `publishing Python package
distributions using GitHub Actions
<https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`_.