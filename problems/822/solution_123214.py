def repetidos(lista):
    """Recebe uma lista de números e retorna o número de vezes
       que um elemento da lista é igual ao elemento anterior
       Parâmetro de entrada:list
       Parâmetro de saída:int"""
   
    indice=1
    ocorrencia=0
    while indice<len[lista]:
        if (lista[indice]==lista[indice-1]):
            ocorrencia=ocorrencia+1
        indice=indice+1
    return ocorrencia