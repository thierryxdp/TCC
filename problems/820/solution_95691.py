def posLetra(frase,letra,oc):
    """Função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada
    da letra(1 para ocorrência, 2 para segunda, etc). Sua função deve retornar em que posição da string aquela
    ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1."""
   i = 0
    p = 0
    while(len(frase)>i):
        if frase[i] == letra:
            p = p + 1
        if p == oc:
            return i
        i = i + 1
    return -1