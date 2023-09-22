def filtraMultiplos(lista,n):
    """função que recebe como entrada uma lista de números e um número(n), e retorna uma outra lista contendo todos os elementos da lista original divisíveis por n
    string -> string"""
    multiplos=[]
    indice=0
    while indice<len(lista):
          if lista[indice]%n==0:
             multiplos=multiplos+[lista[indice]]
          indice=indice+1
    return multiplos