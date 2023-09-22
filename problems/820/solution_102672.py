def posLetra(s,letra,num):
    '''
       Funcao que recebe como entrada uma string, uma letra
       e um numero que indica a ocorrencia daquela letra, e
       retorna a posição da string em que a letra está. Caso
       exista menos ocorrencia de letras do que a pedida, a
       função deve retornar -1.

       str,str,int -> int
    '''
    L = 0
    Ocorrencia = 0
    Frase = list(s)

    while len(Frase) > L:
        if letra in Frase[L]:
            ocorrencia += 1

            if ocorrencia == num:
                return L
        L += 1
        if ocorrencia < num:
            return -1
        else:
            return ocorrencia