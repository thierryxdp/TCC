def posLetra(texto,letra,n):
    '''Função que retorna o índice da ocorrência desejada de uma letra em texto, dado o texto, a letra e o número n que indica se é a primeira, a segunda ou outra ocorrência;str,str,int->int'''
    num_de_ocorrencia=0
    indice=0
    if str.count(texto,letra)<n:
            return -1
    while num_de_ocorrencia<n:
        if texto[indice]==letra:
            num_de_ocorrencia=num_de_ocorrencia+1
        indice=indice+1
    return indice-1