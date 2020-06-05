"""
r > somente leitura
w > escrita(caso o arquivo ja exista, ele sera apagado e um novo
arquivo vazio sera criado)
a > leitura e escrita(add o novo conteudo ao fim do arquivo)
r+ > leitura e escrita
w+ > escrita(este modo, igual ao w, tambem apaga o conteudo
anterior do arquivo)
a+ > leitura e escrita(abre o arquivo para atualiação)
"""

w = open("arquivo2.txt", "w") #novo arquivo

w.write("Esse eh meu novo arquivo") #função w acima descrito, e def write para escrever no arquivo

w.close()#fechar o arquivo

print
