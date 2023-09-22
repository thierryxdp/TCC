def uppCons(string):
    """
    Essa função dado uma string como argumento ira retornar as consoantes dessa string em maiusculo
    str->str
    """
    contador = 0
    
    a = list(string)
    while contador < len(string) - 1:
        if a[contador] == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z':
            list.replace(a[contador], str.upper(a[contador]))
    contador = contador + 1
            
        
                          
    return str(a)