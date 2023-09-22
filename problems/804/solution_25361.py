def filtra_pares(tupla):
      '''Essa função dado os parâmetros, filtra os elementos pares
    e retorna uma tupla contendo os elemetos filtrados
    int,int,int,int->tuple'''
lista=[]
 for i in tupla:
    if i%2==0:
       lista.append(i)
    return lista