class AuthService:

    def login(username, password):
        # Hardcoded admin credentials
        admin_username = "admin"
        admin_password = "admin"

        # Check if provided credentials match the hardcoded admin credentials
        if username == 'admin' and password == 'admin':
            return "Login successful! Access granted."
        else:
            raise ValueError("Invalid username or password. Access denied.")
