class AuthManager:
    token = ""

    @staticmethod
    def set_token(new_token):
        AuthManager.token = new_token

    @staticmethod
    def get_token():
        return AuthManager.token
