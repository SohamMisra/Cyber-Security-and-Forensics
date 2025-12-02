import socket

socket_object=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
socket_object.bind(('127.0.0.1',9999))
socket_object.listen(20)

ips=['172.18.3.140','172.16.22.122','41.191.231.21','84.54.82.173','168.119.103.19']
port=['9999','80','23','80','80']

ip_port=dict()
for i,j in zip(ips,port):
 ip_port[i]=j
if __name__ == '__main__':
 while True:
  client_object,address_client=socket_object.accept()
  ip_client,port_client=address_client
  if ip_client in ip_port.keys():
   print("Proxy is requested")
   client_object.close()
  else:
   print(ip_client)
   print("IP connected is legit!!")
   client_object.send(bytes("You are connected to server!!!",'utf-8'))
   client_object.close()