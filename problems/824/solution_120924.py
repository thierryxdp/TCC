def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com todas as letras 
    maiúsculas
    str->str'''

    i=0
    nova_string=''

    while i<len(texto):
        
        if texto[i] in 'abcdefghijklmnopqrstuvwxyz':
            x=texto[i].upper()
        
        elif texto[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            x=texto[i]

        elif texto[i] == ' ':
            x=' '
            
        nova_string=nova_string+x
        i=i+1
        
    return nova_string