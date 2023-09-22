def uppCons(frase):
    '''Função que retorna as consoantes de uma frase
    como letras maiúsculas.
    :param frase:str
    :return:str'''
    
    letras='bcdfghjklmnpqrstvwxyz'
    letra_maiuscula=''
    caract=0
    
    while caract<len(frase):
        if frase[caract] in letras:
            letra_maiuscula=letra_maiuscula+frase[caract].upper()
            
            caract=caract+1
        else:
            letra_maiuscula=letra_maiuscula+frase[caract]
            
            caract=caract+1
            
    return letra_maiuscula