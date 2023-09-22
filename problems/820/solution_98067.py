def posLetra(string,letra,numero):
    
    
    parte= string.split(letra,numero+1)
    if len(parte)<=numero+1:
        return -1
    return len(string)-len(parte[-1])-len(palavra)