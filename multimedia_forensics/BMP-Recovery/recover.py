with open('flag.bmp.broken','rb') as f:
    data = f.read()

f_size=len(data)
i_size=len(data)-0x36
pixels=i_size//3

def recover_img(w,h):
    format_header = """
    42 4D {format_f_size} 00 00 00 00 36 00 00 00 28 00
    00 00 {format_w} {format_h} 01 00 18 00 00 00
    00 00 {format_i_size} 00 00 00 00 00 00 00 00 00 00 
    00 00 00 00 00 00
    """

    header=format_header.format(
        format_f_size=f_size.to_bytes(4,'little').hex(),
        format_i_size=i_size.to_bytes(4,'little').hex(),
        format_w=w.to_bytes(4,'little').hex(),
        format_h=h.to_bytes(4,'little').hex()
    )
    header = bytes.fromhex(header.replace('\n','').replace(' ',''))

    with open(f'recovered_img/{w},{h}.bmp','wb') as f:
        f.write(header)
        f.write(data[len(header):])
    
    

def brute_force():
    for i in range(1,pixels,1):
        if(i*i>pixels):
            break
        if(pixels%i!=0):
            continue
       
        recover_img(i,pixels//i)
        recover_img(pixels//i,i)

brute_force()