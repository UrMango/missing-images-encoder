import os
import base64
import json
import sys
import requests
import csv

# Specify the folder containing your images
folder_path = 'test-images'


def send_put_request(data):
		url = "https://api.iron-swords.com/missing-cases"
		headers = {
        "Content-Type": "application/json"
    }
		try:
				response = requests.put(url, data=json.dumps(data), headers=headers)
				response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx status codes)
				return response
		except requests.exceptions.RequestException as e:
				print(f"An error occurred: {e}")
				return None


# Function to read and encode images to base64
def encode_images_to_base64(folder_path):
		encoded_images = []

		# List all files in the folder
		for filename in os.listdir(folder_path):
				if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
						# Open the image using Pillow
						img_path = os.path.join(folder_path, filename)
						# image = Image.open(img_path)

						# Convert the image to bytes and encode it to base64
						with open(img_path, "rb") as image_file:
								base64_image = base64.b64encode(image_file.read()).decode('utf-8')
								encoded_images.append({
										'name': filename,
										'personId': 'test',
										'contactPhoneNumber': 'test',
										'photoBase64': base64_image
								})

		return encoded_images

encoded_images = encode_images_to_base64(folder_path)

with open("missing-res.json", "w") as f:
	array = []
	count = 1
	for image in encoded_images:
			print(str(count) + "/" + str(len(encoded_images)))
			try:
				result = send_put_request(image)
				json_res = json.loads(result.text).get("missingCase")
				array.append(json_res)
			except:
				pass
			count += 1

	json.dump(obj=array, fp=f)

# with open('students.csv', 'w', newline='') as file:
# 		writer = csv.writer(file)
# 		writer.writerow(["PersonId", "Name", "InputBase64", "TargetBase64" "IsFound", "ContactPhoneNumber", "RekognitionSearchFaces"])
		
# 		for image in encoded_images:
# 			json_res = json.loads(send_put_request(image).text)
# 			print(json_res)
# 			json_res = json_res.get("missingCase")
# 			writer.writerow([
# 				str(json_res.get('personId')), 
# 				str(json_res.get('name')), 
# 				str(image.get('photoBase64')), 
# 				str(json_res.get('photoBase64')), 
# 				str(json_res.get('isFound')), 
# 				str(json_res.get('contactPhoneNumber')), 
# 				str(json_res.get('rekognitionSearchFaces'))])