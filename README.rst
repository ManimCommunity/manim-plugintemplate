Plugin Template
===============
This is a template project that demonstrates how one can create and upload a manim 
plugin to PyPI using a PEP 517 compliant build system (in this case
`poetry <https://python-poetry.org>`_). This build system ensures users of
your plugin are able to do so reliably without without falling into
dependency hell. You may use another build system other than poetry (e.g.
Flit, Enscons, etc...) if you wish to.

Creating Plugins
----------------
Plugins are features that can be used to extend the core of Manim's
functionality. By convention, plugins should be prefixed by ``manim-`` when
being named. This allows users to easily search for plugins on organizations
like PyPi, but it is not required. Manim discovers user plugins via the
metadata specified in the ``pyproject.toml``.

Installing Poetry
~~~~~~~~~~~~~~~~~
Poetry can be installed on any OS that can has curl. Please visit the
official poetry website for `installation instructions
<https://python-poetry.org/docs/#installation>`_.

Setting Up Your Plugin Directory Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a Python project suitable for poetry you may want to see the
official documentation for a list of all `available commands
<https://python-poetry.org/docs/cli/>`_. In short, if you haven't
extended manim's functionality yet, run:

.. code-block:: bash

	poetry new --src manim-YourPluginName 

*Note:* ``--src`` *is both optional and recomended in order to create a src
directory where all of your plugin code should live.*

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
create and populate a ``pyproject.toml`` similar to the one in this template.

See the official documentation 
for more information on the `init command <https://python-poetry.org/docs/cli/#init>`_.

Updating Pyproject.toml
~~~~~~~~~~~~~~~~~~~~~~~
The ``pyproject.toml`` file is used by poetry and other build systems to
manage and configure your project. Manim uses the `package's entry
point metadata
<https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata>`_
to discover available plugins. The entry point, ``"manim.plugins"``, is
**REQUIRED** and can be `specified as
follows <https://python-poetry.org/docs/pyproject/#plugins>`_:

.. code-block:: toml

    [tool.poetry.plugins."manim.plugins"]
    "manim_yourpluginname" = "manim_yourpluginname"

This allows Manim to discover your plugin via ``manim plugin -u``

Testing Your Plugin Locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    poetry install

This command will read the ``pyproject.toml``, install the dependencies of
your plugin, and create a ``poetry.lock`` file to ensure everyone using your
plugin gets the same version of dependencies. It is important that your
dependencies are properly annotated with a version constraint (e.g.
``manim:^0.1.1``, ``numpy:1.19.2``, etc...). Equally important to the
dependencies specified here is that they do not conflict with manim's.

See the official documentation for more information on `versioning
<https://python-poetry.org/docs/dependency-specification/>`_ or the `install
command <https://python-poetry.org/docs/cli/#install>`_. 

Uploading Your Project
----------------------

By default, poetry is set to register the package/plugin to pypi. As soon as
your plugin is useful locally, run the following:

.. code-block:: bash

    poetry publish --build

Your project should now be available on PyPI for users to install via ``pip
install manim-YourPluginName`` and usable within their respective
environments.

See the official documentation for more information on the `publish command
<https://python-poetry.org/docs/cli/#publish>`_.