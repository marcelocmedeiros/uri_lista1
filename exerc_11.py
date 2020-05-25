# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).
 A fórmula para calcular o volume é: (4/3) * pi * R³. Considere (atribua) para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++),
 assumem que o resultado da divisão entre dois inteiros é outro inteiro.

Entrada
O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.

Saída
A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaço antes e
m espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.
'''
r = float(input('Informe o raio: '))
pi = 3.14159

v = (4/3) * pi * r**3

print('VOLUME = {:.3f}'.format(v))


