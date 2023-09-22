def busca(string,matriz):
    busca=[]
    contador=0
    for linha in matriz:
        if string in linha:
            busca+=[linha,]
            busca[contador].remove(string)  
            contador+=1
    return busca