def posLetra(frase,letra,numero):
    """Função que dada uma frase, uma letra e um número retorna em que 
       posição da frase aquela ocorrência da letra está. Caso exista menos
       ocorrências da letra do que a ocorrência pedida, a função deve 
       retornar -1.
       str,str,int->int.
       
       Parâmetros:
       frase: A frase que será avaliada pela função.
       letra: A letra que será contada a posição indicada.
       numero: Um número que indica a ocorrência desejada da letra na frase
       
       Returns: Em qual posição da frase aquela ocorrência da letra está.
       Caso exista menos ocorrências da letra do que a ocorrência pedida,
       a função retorna -1.
    """
    contador = 0
    ocorrencias = 0
    while ocorrencias < numero and contador < len(frase):
        if frase[contador] == letra:
            ocorrencias = ocorrencias + 1
        contador = contador + 1
    if ocorrencias >= numero:
        return contador - 1
    else:
        return -1