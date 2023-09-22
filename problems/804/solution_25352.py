def filtra_pares(tupla):
      '''Essa função dado os parâmetros, filtra os elementos pares
    e retorna uma tupla contendo os elemetos filtrados
    int,int,int,int->tuple'''
a,b,c,d = tupla
a=tupla[0]
b=tupla[1]	
c=tupla[2]
d=tupla[3]
lista=[a,b,c,d]
 for i in lista:
    if i%2==0:
      return (lista.append(i))