# fak-django-template

Bleeding edge `django3.2.9+` and else template focused on ???

---

## Purpose

This project is used to scaffold a `django` project structure.
Just like `django-admin.py startproject` but better or `wemake-django-template` but worse.

## Features

- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- [`pytest`](https://pytest.org/) for unit tests
- [`flake8`](http://flake8.pycqa.org/en/latest/) for linting

## Installation

Zeroely:  [dependencies](https://python-poetry.org/docs/master/#installation):


```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Firstly, you will need to install [dependencies](https://cookiecutter.readthedocs.io/en/latest/):
(installed cookiecutter in some venv)

```bash
pip install cookiecutter
```

Then, create a project itself (in venv):

```bash
cookiecutter <gh:facktorial/fak-django-graphql-jupyterlab-template>
```

```bash
cd <project_name>
poetry install
cd <project name>
```

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py load loadtests.json
poetry run python manage.py runserver
```

Test GraphQl api: on localhost:port/graphql/

```
query {
	allTests {
	    name
		id
		size
		consumers				  
	}	
}
```

Run jupyterlab:

```bash
poetry run python manage.py shell_plus --notebook
```