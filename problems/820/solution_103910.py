def posLetra (frase,letra,n):
    '''
    Função que recebe uma string, uma letra, e um numero,
    e retorna em que posição da string aquela ocorrencia (n)
    de letra está
    str, str, int ---> int
    '''
   
    if str.count(frase,letra)<n:
        return -1
    while ocorrencia==n:
         ocorrencia=0
        tamanho=0
        if letra in frase[tamanho]:
            ocorrencia=ocorrencia+1
        tamanho=tamanho+1
    return tamanho