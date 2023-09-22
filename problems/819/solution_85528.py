def filtraMultiplos(lista):
    n1 = int(input())
n2 = int(input())
soma = 0
count = -1
for c in range(n1, n2, 2):
  if c % 3 == 0:
    soma += c
    count += 1
return ('O numero {} tem {} multiplos menores que {}.'.format(n1, count, n2))