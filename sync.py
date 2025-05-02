import os
import re
import subprocess

# Base directory to search from
base_dir = 'experiments/active-finetuning/homeoffice-da-clipart'
target_date = '20250501'

# Regex to match run folders like: run-20250430_194453-xxxxxxx
run_dir_pattern = re.compile(rf'^run-{target_date}_\d+-\w+$')

# Walk through the directory tree
for root, dirs, files in os.walk(base_dir):
    for d in dirs:
        if run_dir_pattern.match(d) and 'wandb' in os.path.normpath(root).split(os.sep):
            run_path = os.path.join(root, d)
            print(f"Syncing: {run_path}")
            try:
                subprocess.run(['wandb', 'sync', run_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error syncing {run_path}: {e}")
