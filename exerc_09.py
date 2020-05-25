# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e
o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
informar o total a receber no final do mês, com duas casas decimais.
'''

nome = str(input())
s = round(float(input()), 2)
v = round(float(input()), 2)

sf = s + (v * 15 / 100)

print('TOTAL = R$ {:.2f}'.format(sf))
