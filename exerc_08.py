# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
o valor que recebe por hora e calcula o salário desse funcionário.
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''

nf = int(input())
nh = int(input())
vh = round(float(input()), 2)

s = nh * vh

print('NUMBER = {}'.format(nf))
print('SALARY = U$ {:.2f}'.format(s))
