# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado
evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido
para horas:minutos:segundos, conforme exemplo fornecido.
'''

n = int(input('n= '))
h = n // 60**2
n = n - h * 60**2

m = n // 60
n = n - m*60

s = n

print('{}:{}:{}'.format(h, m, s))