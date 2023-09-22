def posLetra(frase, string, n):
    '''Funcao recebe uma frase e retorna em que posicao está uma determinada letra apos um certo numero de repetcoes recebido também
string -> int'''
    contador = 0
    repetiu = 0
    while (repetiu != n  and contador < len(frase)):
        if (frase[contador] == string):
            repetiu += 1
        contador += 1
    if (repetiu < n):
        return -1
    else:
        return contador -1