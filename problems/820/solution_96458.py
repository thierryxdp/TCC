def posLetra(string,letra,ocorrencia):
    total_de_ocorrencias = str.count(string,letra)
    i = 0 
    if total_de_ocorrencias < ocorrencia:
        return -1
    
    while i < len(string):
        str.index(string,letra,i)
        return str.index(string,letra,i)