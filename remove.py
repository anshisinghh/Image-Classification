import os

# Define the path to your data folder
data_folder = './data'

# Define the minimum file size threshold (20KB)
min_file_size_kb = 30

# Convert KB to bytes
min_file_size_bytes = min_file_size_kb * 1024

# Function to delete images smaller than the threshold
def delete_small_images(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Check if the file is an image and smaller than the threshold
                if os.path.getsize(file_path) < min_file_size_bytes and file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    print(f"Deleting {file_path} ({os.path.getsize(file_path)} bytes)")
                    os.remove(file_path)
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")

# Run the function on your data folder
delete_small_images(data_folder)
