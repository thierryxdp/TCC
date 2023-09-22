def filtraMultiplos(lista,n):
'''recebe uma lista de numeros e um numero e retorna uma lista com os elementos divisiveis por n'''
'''list,int -> list'''
lista2 = []
i = 0
while i<len(lista):
if lista[i]%n == 0:
lista2 = lista2 + [lista[i]]
i = i + 1
return lista2