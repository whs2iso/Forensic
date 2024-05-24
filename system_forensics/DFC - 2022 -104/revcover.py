import base64

data=""

for i in range(1,38,1):
    file = str(i)+".bin"
    with open(file,"r") as f:
        data += f.read()

f = open('result.pdf','wb')

data_byte=data.encode('utf-8')
data_base64=base64.b64decode(data_byte)

f.write(data_base64)
f.close()