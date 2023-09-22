def substitui(s,x,i):
    """A função substiruirá o elemento da posição 'i' pelo caractere 'x' 
    dentro da string escolhida
    Entrada: String, Int, Int
    Saída: String"""
    i = x
    novastr1 = len(s)//2
    novastr2 = s[:i]
    novastr3 = s[i:]
    return novastr2 + x + novastr3