import socket
import threading
def reverse_string(s):
    return s[::-1]
def read_and_reversewrite(input_file,output_file):
    try:
        with open(input_file,"r") as f:
            content=f.read()
            rev_content=reverse_string(content)
            with open (output_file,"w") as f1:
                f1.write(rev_content)
    except FileNotFoundError:
        print(f"{input_file} not found")
    except PermissionError:
        print(f"Permissions not enabled for file read/write to {input_file}")
    except Exception as e:
        print(f"An unexpected error occurred:{e}")
def simple_server(port):
    socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.bind(('localhost',port))
    socket_server.listen(1)
    print(f"Server listening to port {port} ...")
    while True:
        conn,addr=socket_server.accept()
        print(f"Connection from {addr}")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            print(data)
        conn.close()
server_thread=threading.Thread(target=simple_server,args=(65435,))
server_thread.start()
input_str="Hello,World !"
reversed_str=reverse_string(input_str)
print(f"Original string:{input_str}")
print(f"Reversed string:{reversed_str}")
read_and_reversewrite('input.txt','output.txt')