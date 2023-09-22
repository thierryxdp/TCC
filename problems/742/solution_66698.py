def substitui(s,x,i):
    """Retorn uma string igual a s,exceto que o elemento da posição i deve ser substituído pelo caractere x"""
    primeira_parte=s[:i]
    segunda_parte=s[i+1:]
    return primeira_parte+x+segunda_parte