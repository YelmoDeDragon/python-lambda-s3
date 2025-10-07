import requests
import base64


class ImageManager:
    def __init__(self):
        self.my_url = "http://photo-album-alb-2008665684.us-east-2.elb.amazonaws.com"
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": "1234567890"
        }
    
    def create_image(self, file_data: str):
        body = {
            "file_id": "example.txt",
            "file_content": file_data
        }
        try:
            response = requests.post(f"{self.my_url}", json=body, headers=self.headers)
            print("----- Response Status Code:", response.status_code)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error creating image: {e}")
            return None
        

image_handler = ImageManager()

with open("example.txt", "rb") as f:
    text_bytes = f.read()
    encoded = base64.b64encode(text_bytes).decode('utf-8')
    result = image_handler.create_image(encoded)
    print("Image created:", result)
