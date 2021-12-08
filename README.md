# djangocms-navigation
A series of plugins based on the navigation/menu for django-cms.org

Project is using pre-commit for code quality. Packages required to aid development are in the root requirements.

After setting up a virtual environment and installing these packages please make sure you install the hooks.

To clarify these steps;

```
pip install -r requirements.txt
pre-commit install
```

After the initial install you'll also have `pip-tools` which is managing version of packages and dependencies of
the required apps. The available commands for this include;

```
pip-compile  # compiles the `requirements.in` file to produce `requirements.txt`
pip-compile -U  # Upgrade the requirements and compiles them to produce `requirements.txt`
pip-sync  # sync your installed packages with what is required by the project
```
