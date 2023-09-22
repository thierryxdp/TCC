def posLetra(frase,letra,n):
    """Esta é a função que dada uma frase, uma letra e um número da ocorrência desejada da letra, retorna o índice da n ocorrência da letra, caso o n seja maior que o número de ocorrências o retorno será -1; str, str, int => int"""    
    i = 0
    ocorrencia = 0
    count = frase.count(letra)

    if n > count:
        return -1
    
    else:

        while ocorrencia < n:

            if frase[i] == letra:
                ocorrencia = ocorrencia + 1
                i = i + 1
            else:
                i = i + 1
            
    return i - 1