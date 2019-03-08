import socket, time, pickle, psutil

# Função que imprime a lista formatada
def menu_cliente():

    print("Digite a seguinte tecla para ter informações do servidor:\n"
          "\t [1] Informação do Processador \n"
          "\t [2] Informação da Memória \n"
          "\t [3] Informação do Disco \n"
          "\t [4] Informação da CPU \n"
          "\t [5] Informação do Diretório \n"
          )

menu_cliente()

a = input("Digite o número da informação que deseja saber: ")


# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  # Tenta se conectar ao servidor
  s.connect((socket.gethostname(), 9999))
  msg = str(a)
  print('{:>8}'.format('%CPU')+'{:>8}'.format('%MEM'))
  for i in range(10):
      # Envia mensagem vazia apenas para indicar a requisição
      s.send(msg.encode('ascii'))
      bytes = s.recv(6000)

      # Converte os bytes para lista
      lista = pickle.loads(bytes)
      print(lista)
      time.sleep(2)

  msg = 'fim'
  s.send(msg.encode('ascii'))

except Exception as erro:
  print(str(erro))

# Fecha o socket
s.close()

input("Pressione qualquer tecla para sair...")
