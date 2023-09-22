def concatenacao(a, b):
    """Essa função apenas concatena as strings de forma simétrica em
    relação ao metade geométrica da nova string formada. Especificamente,
    suponha dois inputs, transforma eles strings (mas como o enunciado
    pede que a e b sejam strings considere que os inputs serão apenas
    strings) e os concatena na forma abba.
    Assinatura: str,str -> str
    testes: 
    concatenacao('a','b')=='abba'
    concatenacao('ab','ab')=='abababab'
    concatenacao('ROBERTOCARLOS','CLAUDIALEITE')=='ROBERTOCARLOSCLAUDIALEITECLAUDIALEITEROBERTOCARLOS'
    
    """
    return str(a)+str(b)+str(b)+str(a)