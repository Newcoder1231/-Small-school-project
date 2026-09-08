def create_account(name, age, country, language):
    account = f"Name: {name}, Age: {age}, Country: {country}, Language: {language}"
    return account


name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
language = input("Enter your language: ")

account_info = create_account(
    language=language,
    name=name,
    country=country,
    age=age
)

print("\nAccount created!")
print(account_info)