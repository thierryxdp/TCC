def intercala(lista1,lista2):
   	'''
    Funçao que gera uma 3a lista com elementos intercalados de 2 outras listas
    de tamanho 3 cada.
    lista1 -> elementos lista 1
    lista2 -> elementos lista 2

    (list[str,str,str], list[int,int,int]) -> list[str,str,str,str,str,str]
    '''
    return[lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]