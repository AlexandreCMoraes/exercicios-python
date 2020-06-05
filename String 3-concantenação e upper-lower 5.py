#CONCATENAÇÃO DE STRING E BUSCANDO UMA SUBSTRING

minha_string = "O rato roeu a roupa do rei de Roma"

busca = minha_string.find("rei")#lembrando que contagem a partir do 0

print(busca)

#ou

print(minha_string[busca:])#busca as palavras depois da 'busca' "rei"
#se nao acha a palavra é retornado -1