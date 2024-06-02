import cv2
import pytesseract
import os
import csv

# 프레임 이미지가 저장된 폴더 경로
frames_folder = 'C:/Users/a0104/Downloads/DFC2023-20240530T025420Z-001/DFC2023'
# 출력 CSV 파일 경로
output_csv = 'output.csv'

# Tesseract 실행 파일 경로 (Windows 경로 예시)
pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'

# 주어진 이미지에 OCR을 수행하는 함수
def ocr_image(image_path):
    # 이미지를 읽어옵니다
    img = cv2.imread(image_path)
    # 이미지를 RGB로 변환합니다 (OpenCV는 기본적으로 BGR을 사용합니다)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # OCR을 수행합니다
    text = pytesseract.image_to_string(img_rgb, lang='eng')
    return text

# OCR 결과를 저장할 리스트
ocr_results = []

# 폴더 내 모든 프레임 이미지를 순회합니다
for frame_file in os.listdir(frames_folder):
    if frame_file.endswith('.jpg'):
        frame_path = os.path.join(frames_folder, frame_file)
        # 프레임에 OCR을 수행합니다
        ocr_text = ocr_image(frame_path)
        # 결과를 리스트에 추가합니다
        ocr_results.append([frame_file, ocr_text])

# OCR 결과를 CSV 파일에 작성합니다
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Frame', 'Text'])
    writer.writerows(ocr_results)

print(f'OCR 결과가 {output_csv} 파일에 저장되었습니다.')
