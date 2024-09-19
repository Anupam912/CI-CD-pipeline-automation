# python/notify.py
import requests
import json
from logger import setup_logger

logger = setup_logger('notify', 'notify.log')

def send_slack_notification(message):
    """Sends a notification to a Slack channel."""
    webhook_url = 'https://hooks.slack.com/services/your/slack/webhook'
    slack_data = {'text': message}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code == 200:
        logger.info(f"Notification sent: {message}")
    else:
        logger.error(f"Failed to send notification: {response.status_code}, {response.text}")

if __name__ == '__main__':
    send_slack_notification("Deployment completed successfully.")
