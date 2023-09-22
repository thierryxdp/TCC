def uppCons(string):
    """
    Essa função, dada uma string como argumento ira retorna-la
    com todas as consoantes em maisculo
    str->str
    """
    contador = 0
    nova_string =''
    while contador <=len(string)-1:
        if string[contador] in 'bcdfghjklmnpqrstvwxyzç':
            nova_string = nova_string + str.upper(string[contador])
        if string[contador] not in 'bcdfghjklmnpqrstvwxçyz':
            nova_string = nova_string + string[contador]
            
        contador+=1
                        
                        
                
    return nova_string