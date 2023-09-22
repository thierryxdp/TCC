#
#
#
#
def posLetra(string,letra,numero):
    i=0
    n_ocorrencia=1
    while i < len(string):
        if n_ocorrencia <= numero:
            if string[i] == letra:
                n_ocorrencia = n_ocorrencia + 1
                i=i+1
    return i
return -1