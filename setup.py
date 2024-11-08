import os
import sys
import platform
import subprocess

# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

def add_to_path_linux():
    # Check which shell the user is using, and modify the appropriate profile file
    home_dir = os.path.expanduser("~")
    shell_config_file = os.path.join(home_dir, '.bashrc')  # default for bash

    if os.path.exists(os.path.join(home_dir, '.zshrc')):
        shell_config_file = os.path.join(home_dir, '.zshrc')  # default for zsh

    # Add the directory to the PATH in the shell configuration file
    with open(shell_config_file, 'a') as f:
        f.write(f'\n# Added by blindssrf setup\nexport PATH="$PATH:{script_dir}"\n')
    
    print(f'Added {script_dir} to PATH in {shell_config_file}. Please restart your terminal or run "source {shell_config_file}"')

def add_to_path_windows():
    # Use setx to add the directory to PATH permanently for Windows
    try:
        subprocess.run(f'setx PATH "%PATH%;{script_dir}"', shell=True, check=True)
        print(f'Added {script_dir} to PATH permanently in Windows. Restart your command prompt or system to apply changes.')
    except subprocess.CalledProcessError as e:
        print(f'Error adding to PATH in Windows: {e}')

def main():
    system_platform = platform.system().lower()

    if system_platform == "windows":
        add_to_path_windows()
    elif system_platform == "linux":
        add_to_path_linux()
    else:
        print("This script currently supports only Windows and Linux systems.")

if __name__ == "__main__":
    main()
