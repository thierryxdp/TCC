def filtra_pares( elem1, elem2, elem3, elem4):
    """Função recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: int, int, int, int
    retorno: int"""
    return  (elem1[-1:] in '2,4,6,8,0', 
             elem2[-1:] in '2,4,6,8,0',
             elem3[-1:] in '2,4,6,8,0' 
            and elem4[-1:] in '2,4,6,8,0')