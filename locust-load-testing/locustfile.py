from locust import HttpUser, between
from tasks.user_tasks import UserTasks
from tasks.auth_tasks import AuthTasks, AuthManager  # Add AuthManager import statement
from utils.config_loader import load_test_config

class ApiUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(load_test_config['min_wait'], load_test_config['max_wait'])

    def on_start(self):
        # Perform login to acquire the token.
        self.login()

    def login(self):
        credentials = {"username": "testuser", "password": "testpassword"}
        with self.client.post("/login", json=credentials, catch_response=True) as response:
            if response.status_code == 200:
                AuthManager.set_token(response.json()['jwtToken'])
            else:
                print("Failed to log in")