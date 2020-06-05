"""
Calculadora
Autor: Ale
Função: fazer contas de adição, subtração, divisão, multiplicação
"""

print("-----Calculadora-----")

#para 'tabular' dentro de uma função (aqui 'while'), pressione 'shift' e clica onde quer que termine a tabulação
#aqui no caso, foi dentro de 'while', entao clica em |num1 = input("Digite o primeiro número: ") >>>
#segurando 'shift' e clica onde quer que termine ( linha 40 - print(operação))

sair = False#quando pedir numero1 e 2 e fizer a conta, vai entrar [s/n] para continuar usando o app

while sair == False:

	num1 = input("Digite o primeiro número: ")
	num1 = int(num1) #faz com que a 'string' se torne um valor inteiro, pois sem o 'int' ele concatena num1(2)+num2(2)=22(errado)
	operador = input("Digite o operador (+ - * /): ")
	num2 = input("Digite o segundo número: ")
	num2 = int(num2)

	# + soma
	if operador == "+":
		operação = num1 + num2

	# - subtração
	if operador == "-":
		operação = num1 - num2

	# * multiplicação
	if operador == "*":
		operação = num1 * num2

	# / subtração
	if operador == "/":
		operação = num1 / num2

	print("Resultado: ")
	print(operação)


	teste = input("Deseja sair? [s/n]: ")
	if teste == "s":
		sair = True
		print("Programa Encerrado!")
