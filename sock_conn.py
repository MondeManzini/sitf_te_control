import socket

# -----------Connection Settings--------------
PORT = 5025             # default SMB R&S port 
HOST = '10.8.88.166'    # 
#---------------------------------------------

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(1)
    if s:
        print(s,"Connection succesful.")
except Exception as e:
    print(e,"Check to see if the port number is {PORT}")