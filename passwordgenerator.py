import random
import string

length = int(input('Enter the length of the password (no. of characters): '))

# Define Data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# Combine Data
all_data = lower + upper + numbers + symbols

# Use random on data
temp = random.sample(all_data,length)

# Create password
password = ''.join(temp)

print("You're generated password is: " + password)
