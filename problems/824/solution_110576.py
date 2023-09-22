def uppCons(frase):
    '''função que recebe uma frase e retorna essa mesma frase
    com todas as suas consoantes com letra maiúscula.
    tipo de entrada: str
    tipo de saída: str'''
    
    alfabeto = 1
    frase_final = frase[0].upper()
    
    while alfabeto < len (frase):
        if frase[alfabeto] in ('b','B','c','C''ç','d','D','f','F','g','G','h','H',
           'j','J','k','K','l','L','m','M','n','N', 'p','P','q','Q','r','R','s','S','t','T','v','V','w','W',
           'x','X','y','Y','z','Z'):
            
            frase_final += frase[alfabeto].upper()
        else:
            frase_final += frase[alfabeto].lower()
        alfabeto += 1

    return frase_final