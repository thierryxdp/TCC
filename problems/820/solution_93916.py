def posLetra(frase,letra,num):
    '''Retorna a posição na string de uma letra, dada a string, a letra e o
    número da ocorrência dessa letra, caso exista menos ocorrências ou
    não tenha a letra na string retorna -1 string -> int'''
    i = 0
    ocorrencias = 0
    if (letra in frase):
    	while (ocorrencias < num) and (i < len(frase)):
            if (frase[i] == letra):
                ocorrencias = ocorrencias + 1
            i = i + 1
        if (ocorrencias == num):    
            return i -1
        elif (ocorrencias < num):
            return -1
    else:
        return -1