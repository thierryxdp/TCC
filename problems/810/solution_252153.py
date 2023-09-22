def inverte(f):
    """Retorna a frase f, invertida, em minúsculas e sem pontuação.
    str -> str"""
    f2 = f.split(",")
    f2 = ''.join(f2)
    f2 = f2.split(".")
    f2 = ''.join(f2)
    f2 = f2.split("!")
    f2 = ''.join(f2)
    f2 = f2.split("?")
    f2 = ''.join(f2)
    f2 = f2.split("-")
    f2 = ' '.join(f2)
    
    f2 = f2.lower()
    
    f3 = f2.split()[::-1]
    
    return ' '.join(f3)