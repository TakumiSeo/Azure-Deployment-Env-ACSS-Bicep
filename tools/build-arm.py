import os
import subprocess
from pathlib import Path

def compile_bicep_to_arm(bicep_file_path, output_dir):
    arm_file_path = os.path.join(output_dir, 'az_deploy.json')
    cmd = f'az bicep build --file {bicep_file_path} --outfile {arm_file_path}'

    try:
        subprocess.run(cmd, check=True, shell=True)
        print(f'Successfully compiled {bicep_file_path} to {arm_file_path}')
    except subprocess.CalledProcessError as e:
        print(f'Failed to compile {bicep_file_path} to ARM template. Error: {e}')

def main():
    bicep_file_path = Path.cwd() / 'Environments' / 'main.bicep'
    output_dir = Path.cwd() / 'Environments' 
    compile_bicep_to_arm(bicep_file_path, output_dir)

if __name__ == '__main__':
        main()