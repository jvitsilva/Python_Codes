'''
Exercício: 
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do exercito. 
Para entrar no exercito é preciso ter mais de 18 anos, 
pesar 60 kilos ou mais e medir 1,70 m ou mais.
''' 

idade = int(input('Digite sua idade:'))
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))

if idade>=18 and peso>=60 and altura>=1.70:
	print('Parabéns! Você está apto para entrar no exército')

else: print('Que pena, você não está apto para o exército')	

