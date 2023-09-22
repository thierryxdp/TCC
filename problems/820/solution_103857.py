def posLetra(frase, letra, numero):
    """Função que recebe como entrada uma string, uma letra
    e um número que indica a ocorrência desejada da letra
    (1 para primeira ocorrência, 2 para segunda, etc), e 
    retorna em que posição da string aquela ocorrência da
    letra está. Caso exista menos ocorrências da letra do
    que a ocorrência pedida, a função retornará -1.
    str, str, int -> int"""
    if str.count(string, letra) < numero:
        return -1
    else:
        i = 0
        letras = []
        caracteres = list(frase)
        while i < len(caracteres) and len(letras) < numero:
            if letra == caracteres[i]:
                list.append(letras, caracteres[i])
            i = i + 1
        return i - 1