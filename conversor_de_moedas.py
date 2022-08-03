print('###CONVERSOR DE MOEDAS###\n\n')
print('ESCOLHA A MOEDA DESEJADA:\n')
print('f - Franco suíço\nl - Libra')
print('d - Dólar\nm - Marco alemão')

escolha = str(input('\n\nEscolha a moeda: '))
valor = float(input('Digite o valor em reais a ser convertido: '))
real = 0


if escolha == 'f':
    real = float(valor * 0.18)
    print('Valor em Franco suíço: ' + str(real))
    
if escolha == 'l':
    real = float(valor * 0.16)
    print('Valor em Libra: ' + str(real))    

if escolha == 'd':
    real = float(valor * 0.19)
    print('Valor em Dólar: ' + str(real))    

if escolha == 'm':
    real = float(valor * 0.37)
    print('Valor em Marco alemão: ' + str(real))
