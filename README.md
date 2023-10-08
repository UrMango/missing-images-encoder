# Find Missing People Images in Photos and Videos Database

This script is designed to process a folder of images, encode them into base64 format, and then send them as JSON payloads to an API endpoint for further processing. It is primarily intended for use with images related to missing persons or objects. This README will provide an overview of how to use the script and its functionality.

## Prerequisites

You can install the required packages using pip by running the following command in your terminal:

    ```
    pip install requests
    ```

## Usage

Follow these steps to use the script:

1. **Folder Setup**: Place the images you want to process in a folder named 'images' within the same directory as the script. Ensure that the images are in one of the following formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, or `.gif`.

2. **API Endpoint Configuration**: Modify the `url` variable in the script to point to the API endpoint where you want to send the encoded images. You may need to adjust the `headers` as well, depending on the API requirements.

   ```python
   url = "https://api.iron-swords.com/missing-cases"
   headers = {
       "Content-Type": "application/json"
   }
   ```

3. **Run the Script**: Execute the script by running it from your terminal or code editor. It will read the images from the 'test-images' folder, encode them into base64 format, and send them as JSON payloads to the specified API endpoint.

   ```python
   python encoder.py
   ```

4. **Results**: The script will print progress messages as it processes each image. Successfully processed images will be added to an array named `array`. The JSON data for these images will be saved to a file named "missing-res.json."

## Additional Features (Optional)

The script contains some commented-out code that allows you to save the results in a CSV file. If you wish to use this feature, uncomment the code and modify it as needed to match your requirements.

## Troubleshooting

- If you encounter any errors while running the script, make sure that your Python environment is properly set up and that the required packages are installed.

- Verify that the API endpoint and headers are configured correctly.

- Ensure that the 'test-images' folder contains valid image files in the supported formats.

## Disclaimer

This script is provided as-is, and the user is responsible for complying with all legal and ethical guidelines when using it. Be sure to have the necessary permissions and rights to use any data or images processed by this script.

## License

This script is released under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.
