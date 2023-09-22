def busca(string,matriz):
    busca=[]
    for linha in matriz:
        contador=0
        if string in linha:
            busca+=[linha,]
            busca[contador].remove(string)  
        contador+=1
    return busca