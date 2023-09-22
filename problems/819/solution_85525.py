def filtraMultiplos(lista, n):
    '''funcao que recebe uma lista com numero e retorna outra contendo todos os elementos da lista que forme divisiveis pelo numero adicionado'''
    a=0
    resultado=[]
    while a<len(lista):
            if lista[a]%n==0:
                list.append(resultado, lista[a])
            a=a+1
    return resultado