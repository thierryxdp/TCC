def posLetra(string,letra,ocorrencia):
    total_de_ocorrencias = str.count(string,letra)
    if total_de_ocorrencias < ocorrencia:
        return -1