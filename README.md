# Random User Information Generator

## Overview

This project fetches random user information from an API and displays various details such as name, gender, date of birth, email, phone, cell, location, and ID. The project uses the `requests` library to make HTTP requests and the `random` library to select a random user from the fetched data.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Code Explanation

### Importing Libraries

```python
import requests
import random
```

- `requests`: This library is used to make HTTP requests to the API.
- `random`: This library is used to generate a random number to select a random user from the fetched data.

### Fetching Data from the API

```python
url = 'https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=500'
response = requests.get(url).json()
```

- `url`: The URL of the API that provides random user data.
- `response`: The JSON response from the API is stored in this variable.

### Helper Functions

#### Get User Name

```python
def get_usr_name(raw_data):
    title = raw_data['name']['title']
    first_name = raw_data['name']['first']
    last_name = raw_data['name']['last']
    full_name = f"{title}. {first_name} {last_name}"
    return full_name
```

This function extracts and formats the full name of the user from the raw data.

- `title`: The title of the user (e.g., Mr., Ms.).
- `first_name`: The first name of the user.
- `last_name`: The last name of the user.
- `full_name`: The formatted full name.

#### Get User Date of Birth

```python
def get_usr_dob(raw_data):
    dob = raw_data['dob']['date'][:10]
    age = raw_data['dob']['age']
    return f"{dob} ({age} yrs)"
```

This function extracts the date of birth and age of the user from the raw data.

- `dob`: The date of birth (formatted as YYYY-MM-DD).
- `age`: The age of the user.

#### Get User Location Data

```python
def get_usr_geo_data(raw_data):
    city = raw_data['location']['city']
    state = raw_data['location']['state']
    country = raw_data['location']['country']
    country_code = raw_data['nat']
    zip_code = raw_data['location']['postcode']
    return city, state, f"{country} ({country_code})", zip_code
```

This function extracts location details of the user from the raw data.

- `city`: The city where the user lives.
- `state`: The state where the user lives.
- `country`: The country where the user lives.
- `country_code`: The country code of the user's nationality.
- `zip_code`: The postal code of the user's location.

### Checking Response Status

```python
status_check = response['success']
```

This variable checks if the response from the API indicates success.

### Main Logic

```python
if status_check and 'data' in response:
    rndm_num = random.randint(0, 499)
    random_usr_raw_data = response['data']['data'][rndm_num]

    name = get_usr_name(random_usr_raw_data)
    gender = random_usr_raw_data['gender']
    email_addrs = random_usr_raw_data['email']
    dob = get_usr_dob(random_usr_raw_data)
    phone = random_usr_raw_data['phone']
    cell = random_usr_raw_data['cell']
    city, state, country, zip_code = get_usr_geo_data(random_usr_raw_data)
    id = random_usr_raw_data['id']

    print(f"Name : {name}\nGender : {gender}\nDoB/Age : {dob}\nEmail : {email_addrs}\nPhone : {phone}\nCell : {cell}\nCity : {city}\nState : {state}\nCountry : {country}\nPostcode : {zip_code}\nID : {id}")

else:
    print("Received Bad Response from API, please try again")
```

- `status_check and 'data' in response`: Checks if the API response is successful and contains the required data.
- `rndm_num = random.randint(0, 499)`: Generates a random number between 0 and 499 to select a random user.
- `random_usr_raw_data`: Stores the data of the randomly selected user.
- The following lines extract various details of the user using the helper functions and directly from the raw data.
- `print()`: Displays the extracted user information.

If the response from the API is not successful, it prints an error message.

## Usage

1. Make sure you have Python installed on your system.
2. Install the `requests` library using `pip install requests`.
3. Run the script to fetch and display random user information.

```bash
python main.py
```
