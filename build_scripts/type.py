#!/usr/bin/env python3
import subprocess

bash_command = "poetry run mypy ./src && poetry run mypy ./tests"
subprocess.run(bash_command, shell=True, check=True)
