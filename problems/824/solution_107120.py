def uppCons(frase):
    """Dada uma frase, a função retorna essa mesma frase com todas as consoantes
    em maiúsculas sem modificar os demais caracteres;
    str -> str"""
    frase1 = ''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            frase1 = frase1 + frase[i].upper() 
        else: 
            frase1 = frase1 + frase[i]
        i = i + 1    
    return frase1