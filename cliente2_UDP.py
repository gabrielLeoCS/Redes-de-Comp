from socket import socket, AF_INET, SOCK_DGRAM, timeout

IP_Servidor = '127.0.0.1' 
# Endereco IP do Servidor
             
PORTA_Servidor = 5000                  
# Porta em que o servidor estara ouvindo

MEU_IP = ''                                
# Endereco IP '' = significa que ouvira em todas as interfaces

MINHA_PORTA = 12000
# Porta que o cliente2 vai ouvir

cliente2 = socket(AF_INET, SOCK_DGRAM)
#  socket.SOCK_DGRAM=usaremos UDP

cliente2_serv = (MEU_IP, MINHA_PORTA) 
cliente2.bind(cliente2_serv)
# faz o bind do ip e a porta para que possa comecar a ouvir
print("O cliente2 está ligado!")

DESTINO = (IP_Servidor, PORTA_Servidor) 
#destino(IP + porta) do Servidor

while(True):
    Mensagem_Recebida, END_cliente = cliente2.recvfrom(1024)
    mensagem = Mensagem_Recebida.decode("utf-8")
    seq = mensagem[:1]
    mensagem = mensagem[1:]
    

    
    if(mensagem == "quit"):
        print("Encerrando comunicação...")
        break

    if len(Mensagem_Recebida) is not None:
        print ("Recebi =", mensagem,", do cliente", END_cliente, "\n")
        # endereco eh o endereco do socket que enviou os dados.           

    Mensagem = "ACK"

    cliente2.sendto (str(seq).encode() + Mensagem.encode(), DESTINO)
    # enviar a mensgem para o destino(IP + porta)
    # bytes(Mensagem,"utf8") = converte tipo  str para byte
          
cliente2.close()
# fim socket
