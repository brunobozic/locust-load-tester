from locust import TaskSet, task
from utils.config_loader import endpoints, credentials
from utils.auth import AuthManager
from utils.logger import logger

class AuthTasks(TaskSet):

    @task
    def login(self):
        try:
            with self.client.post(endpoints['login'], json=credentials, catch_response=True) as response:
                if response.status_code == 200:
                    AuthManager.set_token(response.json()['jwtToken'])
                else:
                    response.failure(f"Failed to log in: {response.text}")
                    logger.error(f"Login failed: {response.status_code} - {response.text}")
        except Exception as e:
            logger.exception("Login request failed.")
