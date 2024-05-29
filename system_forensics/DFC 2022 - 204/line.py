# filter_empty_lines.py
input_file = 'usbdata1.txt'
output_file = 'filtered_capdata.txt'
 
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        if line.strip():  # 공백이 아닌 줄만 필터링
            outfile.write(line)
