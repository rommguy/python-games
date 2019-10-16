#!/usr/bin/env python3
import subprocess

bash_command: str = "python ./build_scripts/lint.py && python ./build_scripts/type.py && python ./build_scripts/test.py"
subprocess.run(bash_command, shell=True, check=True)
