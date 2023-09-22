def filtra_pares(t):
    '''
    Funcao que recebe uma tupla com quatro inteiros e retorna uma nova tupla contendo apenas os inteiros pares da tupla original na mesma orden que se encontravam.
    Parâmetro:
    	t: tuple
    Saída:
    	tuple
    '''
    tupla = ()
    if t[0]%2 == 0:
        tupla = tupla + (t[0],)
    if t[1]%2 == 0:
        tupla = tupla + (t[1],)
    if t[2]%2 == 0:
        tupla = tupla + (t[2],)
    if t[3]%2 == 0:
        tupla = tupla + (t[3],)
    return tupla