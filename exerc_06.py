# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e
a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
'''

a = round(float(input()), 1)
b = round(float(input()), 1)
c = round(float(input()), 1)

m = (a*2 + b*3 + c*5)/10

print('MEDIA = {:.1f}'.format(m))
