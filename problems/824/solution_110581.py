def uppCons(frase):
    '''função que recebe uma frase e retorna essa mesma frase
    com todas as suas consoantes com letra maiúscula.
    tipo de entrada: str
    tipo de saída: str'''
    
    alfabeto = 1
    frase_final = frase[0].upper()
    
    while alfabeto < len (frase):
        if frase[alfabeto] in ('b','c','C','ç','d','f','g','h',
           'j','k','l','m','n', 'p','q','r','s','t','v','w',
           'x','y','z'):
            
            frase_final += frase[alfabeto].upper()
        else:
            frase_final += frase[alfabeto].lower()
        alfabeto += 1

    return frase_final