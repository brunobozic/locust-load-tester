from locust import HttpUser, between
from tasks.user_tasks import UserTasks
from tasks.auth_tasks import AuthTasks, AuthManager  # Add AuthManager import statement
from utils.config_loader import load_test_config

class ApiUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(load_test_config['min_wait'], load_test_config['max_wait'])
    def on_start(self):
        # Initialize an instance of AuthTasks and perform login.
        auth_tasks = AuthTasks(self.client)
        auth_tasks.login()

        # Optionally, check if the token was successfully acquired.
        if not AuthManager.get_token():
            # Handle the case where login failed, such as stopping this user.
            self.stop(True)

