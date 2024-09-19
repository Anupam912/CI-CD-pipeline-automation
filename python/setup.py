# python/setup.py
import os
import subprocess
from logger import setup_logger

logger = setup_logger('setup', 'setup.log')

def create_virtual_env():
    """Creates a virtual environment and installs dependencies."""
    if not os.path.exists('venv'):
        subprocess.run(['python3', '-m', 'venv', 'venv'])
        logger.info("Virtual environment created.")
    else:
        logger.info("Virtual environment already exists.")

def install_dependencies():
    """Installs dependencies using requirements.txt."""
    result = subprocess.run(['venv/bin/pip', 'install', '-r', 'requirements.txt'], capture_output=True)
    if result.returncode == 0:
        logger.info("Dependencies installed successfully.")
    else:
        logger.error(f"Error installing dependencies: {result.stderr}")

if __name__ == '__main__':
    create_virtual_env()
    install_dependencies()
