# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e
calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = raiz quadrada de (x2 -x1)² + (y2 -y1)²

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e
a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''
# para receber dois valores em uma linha só
p1 = input('n= ').split()
x1 = float(p1[0])
y1 = float(p1[1])

p2 = input('m= ').split()
x2 = float(p2[0])
y2 = float(p2[1])

d = ( (x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** (1/2)

print('{:.4f}'.format(d))

"""
1.0 7.0
5.0 9.0
"""