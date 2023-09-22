def substitui(s,x,i):
    """Recebendo uma string s, um caractere x e um numero inteiro i
    retorna uma string igual a s, exceto que o elemento da posicao i
    e substituido pelo caractere x"""
    #variavel s e x precisam ser strings e i um inteiro
    stringSub=s[0:i]+x+s[i:len(s)]
    return stringSub