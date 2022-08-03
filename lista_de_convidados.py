'''
EXERCÍCIO: Faça um programa que leia a quantidade de pessoas que
serão convidadas para uma festa. Após isso o programa irá perguntar
o nome de todas as pessoas e colocar numa lista de convidados.
Após isso, irá imprimir todos os nomes da lista.
'''

convidados = input('Digite a quantidade de pessoas convidadas:')
lista_de_convidados = []
nomes = str
i=1
while i<=int(convidados): 
	nomes = input('Coloque o nome do convidado ' + str(i) +': ')
	lista_de_convidados.append(nomes)
	i += 1  

print('\nCONVIDADOS:')
for convidados in lista_de_convidados:
	print(convidados)
