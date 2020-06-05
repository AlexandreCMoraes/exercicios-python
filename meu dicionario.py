meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

print(meu_dicionario["C"]) #imprime o que esta guardado no dicionario
print(meu_dicionario) #imprime todo o dicionario

for chave in meu_dicionario:
	#print(meu_dicionario[chave]) #chave são as letras sozinhas
	print(chave+"-"+meu_dicionario[chave]) #pode ser feito desta maneira tbm

for i in meu_dicionario.items():
	print(i)