"""
Day 1 - Python Fundamentals
Author: Boobalan
Description: A simple CLI program that collects user information
             and displays it in a formatted way.
"""

def user_info():
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Which city do you live in? ")
    country = input("Where do you live? ")

    return {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }
def display_user_info():
    print("\n====User information====")
    print(f'Name: {user_info()["name"]}')
    print(f'Age: {user_info()["age"]}')
    print(f'City: {user_info()["city"]}')
    print(f'Country: {user_info()["country"]}')
    print("=================================")

def main():
    """Main Execution"""
    user = user_info()

    display_user_info()


if __name__ == "__main__":
    main()