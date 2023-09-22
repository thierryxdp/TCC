def carros(capacidade, pessoas = 5):
    tipo = type(capacidade/pessoas)
    if type(capacidade/pessoas) == float:
        return(int(capacidade/pessoas)+1)
    else:
        return int(capacidade/pessoas)
    return (capacidade/pessoas)