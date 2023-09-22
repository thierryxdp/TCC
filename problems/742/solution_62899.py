def substitui(s,x,i):
    """A função substiruirá o elemento da posição 'i' pelo caractere 'x' 
    dentro da string escolhida
    Entrada: String, Int, Int
    Saída: String"""
    novastr1 = len(s)//2
    novastr2 = s[:i]
    novastr3 = s[i:]
    i = x
    return novastr2 + str(x) + novastr3