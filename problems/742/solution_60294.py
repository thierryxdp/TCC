def substitui(s, x, i):
    """Função que retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x
    (str, int, str) -> (str)"""


    return s[0: i] + x + s[(i+1):]