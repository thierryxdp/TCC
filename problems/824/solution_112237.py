def substitui(letra):
    """funcao para transformar uma consoante minuscula em maiuscula;
    str -> str"""
    
    consoantes = ['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    
    if letra in consoantes:
        return str.upper(letra)
    else:
        return letra
    
def uppCons(frase):
    """Dada uma frase de entrada, retorna a mesma frase com todas as consoantes em maiusculo;
    str -> str"""
    
    frase = ''.join(map(substitui,frase))
    
    return frase