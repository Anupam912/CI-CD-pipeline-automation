# python/deploy_status.py
import requests
from logger import setup_logger

logger = setup_logger('deploy_status', 'deploy_status.log')

def check_deployment():
    """Checks if the deployed app is running."""
    try:
        response = requests.get('http://localhost:5000')
        if response.status_code == 200:
            logger.info("Application is running successfully!")
        else:
            logger.warning(f"Application status: {response.status_code}")
    except Exception as e:
        logger.error(f"Failed to reach the application: {e}")

if __name__ == '__main__':
    check_deployment()
