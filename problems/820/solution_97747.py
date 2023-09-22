def posLetra(string,letra,numero):
    """
    
    
    """
    vezes_encontradas = 0
    i = 0
    if str.count(string,letra) >= numero:
        
        while vezes_encontradas != numero:
            
            if string[i] == letra:
                vezes_encontradas = vezes_encontradas + 1
                if vezes_encontradas < numero:
                    i=i+1
            else:
                 i=i+1
        return i
    elif str.count(string,letra)< numero:
        return -1