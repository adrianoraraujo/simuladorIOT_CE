import socket
import thread
from random import randrange, uniform
import time
import re




HOST = '0.0.0.0'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
w, h = 3, 3;
me = [[0 for x in range(4)] for y in range(1)]

arq = open('config.txt', 'r')
ident = arq.readlines()
arq.close()
for t in ident:
    k=t.split(",")
    print(k)
    me[0][0]=str(k[0])
    me[0][1]=int(k[1])
    me[0][2]=str(k[2])
print(me[0][0])
print(me[0][1])
print(me[0][2])
myself=me[0][0]

def conectado(con, cliente):
    print ('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg)
        mesg= str(msg).split(" ")
        remetente=mesg[0]
        pedido=mesg[1]
        destino=mesg[2]
        print(destino)
        print(pedido)

        if(destino!=me[0][0]or destino!="FIM"):
            msg2= "CONEXÂO RECUSADA"+"\n"
            con.send(str.encode(msg2))
            con.close()
            thread.exit()
        
        if(str(pedido)=="STATUS"):
            msg2= me[0][0]+" "+me[0][1]+" "+remetente+"\n"
            con.send(str.encode(msg2))
            con.close()
            thread.exit()

        elif(str(pedido)=="DESCARREGAR"):
            msg2= me[0][0]+" "+"OK"+" "+remetente+"\n"
            con.send(str.encode(msg2))

        elif(str(detino)=="FIM"):
            res= me[0][0]+","+pedido+","+me[0][2]
            arq = open('config.txt', 'w')
            arq.write(res)
            arq.close()
            time.sleep(20)
            print('Finalizando conexao do cliente', cliente)
            con.close()
            thread.exit()
            res= me[0][0]+","+0000+","+me[0][2]
            arq = open('config.txt', 'w')
            arq.write(res)
            arq.close()

                
    print ('Finalizando conexao do cliente', cliente)
    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()
