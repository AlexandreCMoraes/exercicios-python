
arquivo = open("arquivo para teste.txt")

linhas = arquivo.readlines()

for linha in linhas: #> para ler linha por linha(conteudo)
	print(linha)
