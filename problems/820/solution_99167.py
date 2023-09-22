def posLetra(string, letra, n):
    
    teste = str.count(string,letra)
    teste2= str.find(string, letra, n)
    if teste <n:
        return -1
    else:
        return teste2