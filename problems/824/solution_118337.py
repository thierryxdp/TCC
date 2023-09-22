def uppCons(string):
    """
    Essa função dado uma string como argumento ira retornar as consoantes dessa string em maiusculo
    str->str
    """
    
    contador = 0
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    while contador <= len(string):
        if string [contador] == consoantes:
            str.replace(string,string[contador], str.upper(string[contador]))
    contador = contador + 1
            
        
    return string