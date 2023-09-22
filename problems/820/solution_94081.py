def posLetra(frase, letra, numero):
    """ A funçao posLetra recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc). Ela retorna em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
        
        Parameters:
            frase = frase a ser modificada
            letra = letra a qaul sera procurada
            numero = número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc)

        Testes:
            posLetra("") = ""
            posLetra("") = ""
            posLetra("") = ""
            
        Returns:
            posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função retorna -1.
            str, letra, numero --> int
    """
    a=0
    i=0
    numero_repeticoes = str.count(frase,letra)
    if numero_repeticoes < numero:
        return -1
    else:
        while i < numero:
            resultado = str.index(frase,letra,a+1)
            a = resultado
            i = i+1
    return resultado