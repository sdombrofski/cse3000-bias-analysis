# pip install deepface
import os
from deepface import DeepFace       # Facial recognition

def analyze_images_in_directory(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image file extensions
            img_path = os.path.join(directory, filename)
            print(f"Analyzing {img_path}...")
            try:
                result = DeepFace.analyze(img_path, actions=['gender'])  # Gender presentation analysis
                print(f"Results for {filename}: {result}")
            except Exception as e:
                print(f"Error analyzing {filename}: {e}")

# Specify the directory containing the images
image_directory = input("Enter the path to the image directory: ").strip()

# Debugging and normalizing the path
print(f"Debug: Received path: {image_directory}")
image_directory = os.path.abspath(image_directory)
print(f"Debug: Absolute path: {image_directory}")

if os.path.isdir(image_directory):
    analyze_images_in_directory(image_directory)
else:
    print("The provided path is not a valid directory.")

