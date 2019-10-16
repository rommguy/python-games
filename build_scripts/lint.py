#!/usr/bin/env python3
import subprocess

bash_command = "poetry run flake8 ./src && poetry run flake8 ./tests"
subprocess.run(bash_command, shell=True, check=True)
