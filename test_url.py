import requests

my_url = "https://fdp2petvler673ij47ag2lx4hy0izwfy.lambda-url.us-east-2.on.aws/"
response = requests.get(f"{my_url}users/4")  # Call as function

body = {"name": "Laura", "age": 29}
response_2 = requests.post(f"{my_url}users/4", json=body)  # Call as function

# Check response for response 1
if response.status_code == 200:
    try:
        print(response.json())
        print("ggggggggggggg")
    except ValueError:
        print("¿¿¿¿¿¿¿Response 1 is not valid JSON:", response.text)
else:
    print(f"1111Response 1 returned status code {response.status_code}")

# Check response for response 2
if response_2.status_code == 200:
    try:
        print(response_2.json())
    except ValueError:
        print("Response 2 is not valid JSON:", response_2.text)
else:
    print(f"Response 2 returned status code {response_2.status_code}")
