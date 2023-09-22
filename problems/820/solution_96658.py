def posLetra(string, letra, n):
    """
    	Funcao que recebe como entrada um string, uma letra e um numero.
        Retorna a posicao da string em que a letra está, caso exista menos ocorrencias que a 
        pedida retorna -1;
        str, str, int -> int
    """
    lista_pos = []
    i = 0
    while i < len(string):
        if letra == string[i]:
            lista_pos.append(i)
        i = i + 1    
    if len(lista_pos) < n:
        return -1
    
    return lista_pos[n - 1]