from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "Email": fake.email(),
        "ConfirmPassword": "Password1!",
        "DateOfBirth": str(fake.date_of_birth(minimum_age=18, maximum_age=90)),
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Password": "Password1!",
        "UserName": fake.user_name(),
        "Oib": fake.ssn(),  # Replace with appropriate method to generate valid Oib
        "AcceptTerms": True
    }
