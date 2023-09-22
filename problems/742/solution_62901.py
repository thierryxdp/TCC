def substitui(s,x,i):
    """A função substiruirá o elemento da posição 'i' pelo caractere 'x' 
    dentro da string escolhida
    Entrada: String, Int, Int
    Saída: String"""
    novastr1 = s[i:]
    novastr2 = s[:i]
    novastr3 = novastr1[0:] 
    i = x
    return novastr2 + str(x) + novastr3