import os
import subprocess

# Safely update s3 munki repository by always syncing exactly
#  the same directory

bucket = "s3://bk-munki/"

script = os.path.abspath(__file__)
dir_of_script = os.path.dirname(script)
root_of_repo = os.path.abspath(os.path.join(dir_of_script, os.pardir))

os.chdir(root_of_repo)
command = "aws s3 sync " + os.getcwd() + " " + bucket + " --delete"
print(command)
subprocess.call(command, shell=True)
