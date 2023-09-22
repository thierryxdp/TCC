def substitui(s:str,x:int,i:int)->str:
    """recebe uma string 's', um caractere'x' e um inteiro'i' e retorna a mesma
    string 's' só que com o elemento "x" no lugar do elemento da posição 'i'"""
    return s[0:i] + x + s[i + 1:]