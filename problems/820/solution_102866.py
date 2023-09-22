def posLetra(texto, letra, num):
    '''Recebe uma string, uma letra, e um número que indica a ocorrência desejada da letra.
    Retorna em que posição da string aquela ocorrência da letra está. Caso exista menos 
    ocorrências da letra do que a ocorrência pedida, retorna -1;
    string, string, int -> int'''

    i = 0
    posicao = 0
    ocorr = 0

    if str.count(texto, letra) < num:
        return -1

    else:
        while i < len(texto)and ocorr != num:
            if letra in texto[i]:
                posicao = i
                ocorr += 1
            i += 1

        return posicao