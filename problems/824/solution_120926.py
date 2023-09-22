def uppCons(texto):
    '''função que recebe uma frase e retorna a frase com todas as letras 
    maiúsculas
    str->str'''

    i=0
    nova_string=''

    while i<len(texto):
        
        if texto[i] in 'bcdfghjklmnpqrstvwxyz':
            x=texto[i].upper()
            
        else:
            x=texto[i]
            
        nova_string=nova_string+x
        i=i+1
        
    return nova_string