def posLetra(string,letra,numero):
    """
    Recebe uma string, letra e um numero que indica a ocorrencia
    desejada da letra, e retorna em que posição da string aquela
    ocorrência da letra está. Caso ocorra menos ocorrências do que 
    a pedida da letra, a função retorna -1;
    str,str,int->int
    """
    repete = string.count(letra)
    if repete < numero:
        return -1
    elif string[0] != letra and repete >= numero:
        return string.find(letra,numero)
    elif string[0] == letra and repete >= numero:
        return string.find(letra,numero+1)
    else:
        return 'Problema'