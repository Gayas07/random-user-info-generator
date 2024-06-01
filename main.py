import requests
import random

url = 'https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=500'
response = requests.get(url).json()


def get_usr_name(raw_data):
    title = raw_data['name']['title']
    first_name = raw_data['name']['first']
    last_name = raw_data['name']['last']
    full_name = f"{title}. {first_name} {last_name}"
    return full_name


def get_usr_dob(raw_data):
    dob = raw_data['dob']['date'][:10]
    age = raw_data['dob']['age']
    return f"{dob} ({age} yrs)"


def get_usr_geo_data(raw_data):
    city = raw_data['location']['city']
    state = raw_data['location']['state']
    country = raw_data['location']['country']
    country_code = raw_data['nat']
    zip_code = raw_data['location']['postcode']
    return city, state, f"{country} ({country_code})", zip_code


status_check = response['success']
# status_check

if status_check and 'data' in response:
    rndm_num = random.randint(0, 499)
    random_usr_raw_data = response['data']['data'][rndm_num]
    # print(rndm_num)

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
