def posLetra(frase,letra,numero):
    """Funcao que recebe uma string, uma letra e um numero que indica a ocorrencia desejada da letra
    (1 para a primeira ocorrencia, 2 para a segunda, etc), e retorna a posicao em que a string daquela
    ocorrencia esta. Caso exista menos ocorrencias da letra do que a ocorrencia pedida, a funcao deve retornar -1;
    str, str, int -> int"""
    if str.count(frase,letra)<numero:
        return -1
    lista_indices=[]
    contador=0
    while contador<len(frase):
        if frase[contador]==letra:
            lista_indices+=contador
        contador+=1
    return lista_indices[numero-1]