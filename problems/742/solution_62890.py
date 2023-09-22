def substitui(s,x,i):
    """A função substiruirá o elemento da posição 'i' pelo caractere 'x' 
    dentro da string escolhida
    Entrada: String, Int, Int
    Saída: String"""
    x= i
    novastr1 = len(s)//2
    novastr2 = s[:x]
    novastr3 = s[x:]
    
    return novastr2 + x + novastr3