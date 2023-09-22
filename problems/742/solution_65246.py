def substitui(s: str,x: str,i: int)-> str:
    '''retorna uma string igual a s, exceto que o elemento da posição i
    deve ser substituído pelo caractere x'''
    return s[:i] + x + s[(i+1):]