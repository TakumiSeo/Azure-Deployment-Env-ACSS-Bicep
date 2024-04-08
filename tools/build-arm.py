import os
import subprocess
from pathlib import Path
import json

def compile_bicep_to_arm(bicep_file_path, output_dir):
    arm_file_path = os.path.join(output_dir, 'az_deploy.json')
    params_file_path = os.path.join(output_dir, 'az_deploy.parameters.json')
    cmd = f'az bicep build --file {bicep_file_path} --outfile {arm_file_path}'
    params_cmd = f'az bicep params --file {bicep_file_path} --outfile {params_file_path}'

    try:
        subprocess.run(cmd, check=True, shell=True)
        subprocess.run(params_cmd, check=True, shell=True)
        print(f'Successfully compiled {bicep_file_path} to {arm_file_path} and {params_file_path}')

    except subprocess.CalledProcessError as e:
        print(f'Failed to compile {bicep_file_path} to ARM template. Error: {e}')

def main():
    bicep_file_path = Path.cwd() / 'Environments' / 'main.bicep'
    output_dir = Path.cwd() / 'Environments' 
    compile_bicep_to_arm(bicep_file_path, output_dir)

if __name__ == '__main__':
        main()