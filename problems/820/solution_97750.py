def posLetra(string,letra,numero):
    """
    Função que dada uma string, uma letra e um n(número)
    respectivamente, retornara a posição da string em que a 
    n(número/ocorrência da letra) se encontra;
  	Parametro de Estrada: string, string, int;
    Valor de Saida: int.
    """
    vezes_encontradas = 0
    i = 0
    if str.count(string,letra) >= numero:
        while vezes_encontradas != numero:
            
            if string[i] == letra:
                vezes_encontradas = vezes_encontradas + 1
                if vezes_encontradas < numero:
                    i=i+1
            else:
                 i=i+1
        return i
    elif str.count(string,letra)< numero:
        return -1