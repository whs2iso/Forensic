from PIL import Image
import piexif
import glob

def extract_exif_timestamps(image_path):
    img = Image.open(image_path)
    try:
        exif_data = piexif.load(img.info.get('exif', b''))
        date_time_original = exif_data['Exif'].get(piexif.ExifIFD.DateTimeOriginal)
        date_time_digitized = exif_data['Exif'].get(piexif.ExifIFD.DateTimeDigitized)
        date_time_modified = exif_data['0th'].get(piexif.ImageIFD.DateTime)
        
        date_time_original = date_time_original.decode('utf-8') if date_time_original else 'N/A'
        date_time_digitized = date_time_digitized.decode('utf-8') if date_time_digitized else 'N/A'
        date_time_modified = date_time_modified.decode('utf-8') if date_time_modified else 'N/A'
        
        return date_time_original, date_time_digitized, date_time_modified
    except Exception as e:
        print(f"Error reading ExIF data from {image_path}: {e}")
        return 'N/A', 'N/A', 'N/A'

def process_images(directory):
    image_paths = glob.glob(f"{directory}/*.jpg") 
    for image_path in image_paths:
        date_time_original, date_time_digitized, date_time_modified = extract_exif_timestamps(image_path)
        print(f"File: {image_path}")
        print(f"Create Date (DateTimeDigitized): {date_time_digitized}")
        print(f"Date/Time Original: {date_time_original}")
        print(f"Modify Date: {date_time_modified}")
        print()

if __name__ == "__main__":
    directory = "D://forensic//DCIM//Camera"  
    process_images(directory)
