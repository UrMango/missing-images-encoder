import os
import base64
import json

# Specify the folder containing your images
folder_path = 'test-images'

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

# Encode images and print the results
with open("missing.json", "w") as f:
    json.dump(obj=encoded_images, fp=f)
