def posLetra(frase,letra,numero):
   	ocorrencias = str.count(frase,letra,[0:])
    if ocorrencias<numero:
        return ('-1')
    elif ocorrencias >= numero :
    return str.find(frase,letra,numero)