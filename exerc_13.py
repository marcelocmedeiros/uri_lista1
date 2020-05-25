# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos
seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs (a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

maiorAB = (a + b + abs (a-b)) / 2
maiorBC = ((maiorAB + c + abs (maiorAB - c)) / 2)

if(maiorAB > maiorBC):
    print("{:.0f} eh o maior\n".format(maiorAB))
else:
    print("{:.0f} eh o maior\n".format(maiorBC))


