# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e
o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

O arquivo de entrada contém duas linhas de dados.
Em cada linha haverá 3 valores, respectivamente dois inteiros
e um valor com 2 casas decimais.
'''

a, b = input().split(), input().split()
q1 = int(a[1])
v1 = float(a[2])
q2 = int(b[1])
v2 = float(b[2])
t1 = q1 * v1
t2 = q2 * v2
tt = t1 + t2
print('VALOR A PAGAR: R$ %.2f' %tt)
