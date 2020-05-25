# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 03/04/2020

'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

n = int(input('n= '))

n100 = n // 100
r = n % 100

n50 = r // 50
r = r % 50

n20 = r // 20
r = r % 20

n10 = r // 10
r = r % 10

n5 = r // 5
r = r % 5

n2 = r // 2
n1 = r % 2

print(n)
print(n100,'nota(s) de R$ 100,00')
print(n50,'nota(s) de R$ 50,00')
print(n20,'nota(s) de R$ 20,00')
print(n10,'nota(s) de R$ 10,00')
print(n5,'nota(s) de R$ 5,00')
print(n2,'nota(s) de R$ 2,00')
print(n1,'nota(s) de R$ 1,00')
