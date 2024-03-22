collect: pyproject.toml
	caffeinate poetry run collect

process: pyproject.toml
	caffeinate poetry run process