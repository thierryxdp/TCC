def posLetra(string,letra,numero):
    
    
    resultado=-1
    while str.count(string,letra)>numero:
        if numero==1:
            resultado=str.index(string,letra)
            
            
    return resultado