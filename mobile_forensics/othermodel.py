from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data:
        exif_info = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if value is not None:  
                exif_info[tag_name] = value
        return exif_info
    return None

image_path = "D://forensic//DCIM//Camera//20230609_042440.jpg"

exif_info = get_exif_data(image_path)

if exif_info:
    lens_model = exif_info.get('LensModel')
    camera_model = exif_info.get('Model')
    if lens_model is not None:
        print("렌즈 모델 정보:", lens_model)
    else:
        print("이미지 파일에서 렌즈 모델 정보를 찾을 수 없음")
    
    if camera_model is not None:
        print("카메라 모델 정보:", camera_model)
    else:
        print("이미지 파일에서 카메라 모델 정보를 찾을 수 없음")
else:
    print("이미지 파일에서 Exif 데이터를 찾을 수 없음")
