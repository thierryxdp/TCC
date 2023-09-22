def filtraMultiplos(lista,n):
    '''Essa função dadauma lista e um parâmetro n, retorna outra lista com os números multiplos de n,
    list, int-> list'''
    multiplos=[]
    indice=0
    while indice<len(lista):
          if lista[indice]%n==0:
             multiplos=multiplos+[lista[indice]]
          indice=indice+1
    return multiplos