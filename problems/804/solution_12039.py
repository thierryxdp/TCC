def filtra_pares (lista):
    '''funcao que receba uma tupla de 4 elementos e retorne uma nova tupla com os elementos pares da tupla original'''
    lista_pares=list()
    for valor in lista:
        if valor%2==0:
         lista_pares.append(valor)  
        return lista_pares