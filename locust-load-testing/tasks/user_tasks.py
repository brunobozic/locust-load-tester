from locust import task, TaskSet
from utils.config_loader import endpoints
from utils.auth import AuthManager  # Import AuthManager
from utils.logger import logger  # Import the logger
from data.faker_generator import generate_user_data

class UserTasks(TaskSet):

    @task
    def register_user(self):
        user_data = generate_user_data()
        headers = {'Authorization': f'Bearer {AuthManager.get_token()}'}

        try:
            with self.client.post(endpoints['register'], json=user_data, headers=headers, catch_response=True) as response:
                if response.status_code == 201:
                    logger.info("User registered successfully.")
                else:
                    response.failure(f"Failed to register user: {response.text}")
                    logger.error(f"User registration failed: {response.status_code} - {response.text}")
        except Exception as e:
            logger.exception("User registration request failed.")
