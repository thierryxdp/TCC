def posLetra (string,letra,ocorrencia):
    if str.count(string,letra) < ocorrencia:
        return -1
    if ocorrencia == 1:
        return str.index(string,letra)
    else:
        nova_string = str.replace(string,letra,' ',ocorrencia-1)
        return str.index(nova_string,letra)