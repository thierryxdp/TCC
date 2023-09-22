def posLetra (texto, letra, num):
    '''
    	Funcao que recebe uma frase, uma letra e um numero
        que indica a ocorrencia desejada da letra e retorna
        em que posicao da frase aquela ocorrencia da letra
        esta. caso exista menos ocorrencias da letra do que
        a ocorrencia pedida, a funcao retorna -1
        str, str, int -> int
    '''
    i = 0
    ocorrencias = 0
    while i < len(texto):
        if letra in texto[i]:
            ocorrencias += 1
        if ocorrencias == num:
            return i
        i += 1
    if ocorrencias < num:
        return -1
    else: 
        return ocorrencias