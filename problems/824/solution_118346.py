def uppCons(string):
    """
    Essa função dado uma string como argumento ira retornar as consoantes dessa string em maiusculo
    str->str
    """
    
    contador = 0
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    while contador <= len(string)-1:
        if string [contador] == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z':
            str.replace(string , string[contador], str.upper(string[contador]))
        contador = contador + 1
        
       
    return string