# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km)
e o total de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km),
e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".
'''

x = round(float(input('x= ')), 1)
y = round(float(input('y: ')), 1)

v = x / y

print("{:.3f} km/l".format(v))
