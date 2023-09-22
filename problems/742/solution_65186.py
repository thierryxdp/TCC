def substitui(s,x,i):
    """recebe uma string, um caractere e um inteiro e retorna a mesma string, mas com o 
    caractere indicado pelo inteiro substituido pelo caractere recebido"""
    
    string1, string2 = s[:i], s[i+1:]
    
    return string1 + x + string2