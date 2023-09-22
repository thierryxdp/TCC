def eh_quadrada(m):
    """
    Função que recebe uma matriz e identifica se ela é quadrada ou não, retornando True ou False em cada caso de maneira respectiva..
    Parâmetro:
    	m: list
    Saída:
    	bool
    """
    if len(m) == len(m[0]) or len(m) == 0:
        return True
    else:
        return False