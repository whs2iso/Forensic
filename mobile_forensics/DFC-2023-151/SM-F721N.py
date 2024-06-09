from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    
    image = Image.open(image_path)
    
    exif_data = image._getexif()
    
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'Model':
                return value
    return None

def find_different_camera(images_dir):
    import os
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
    
    for image_file in image_files:
        image_path = os.path.join(images_dir, image_file)
        camera_model = get_exif_data(image_path)
        if camera_model != 'SM-F721N':
            return image_path, camera_model
    
    return None, None

images_directory = "D://forensic//DCIM//Camera"

different_image, different_camera_model = find_different_camera(images_directory)

if different_image:
    print("i find the file that pictured other model:")
    print("file path:", different_image)
    print("camera model:", different_camera_model)
else:
    print("other camera's model is 'SM-F721N'")
