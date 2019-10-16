#!/usr/bin/env python3
import subprocess

bash_command = "poetry run pytest"
subprocess.run(bash_command, shell=True, check=True)
