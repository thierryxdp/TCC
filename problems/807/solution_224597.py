def conta_frases(texto):

    lista = ['.',',', '?','!','...' ]
    
    
    return (len(texto[:].split(lista[0])) - 1) +(len(texto[:].split(lista[1])) - 1) +(len(texto[:].split(lista[2])) - 1) +(len(texto[:].split(lista[3])) - 1) +(len(texto[:].split(lista[4])) - 1)