def posLetra(string,letra,numero):
    proximo=0
    ocorrencias=0
    while proximo!=len(string)-1:
        if string[proximo]==letra:
            ocorrencias=ocorrencias+1
        proximo=proximo+1
    if ocorrencias<numero:
        return -1
    else:
        ocorrencias2=0
        proximo2=0
        while numero!=ocorrencias2:
            if string[proximo2]==letra:
                ocorrencias2=ocorrencias2+1
            proximo2=proximo2+1
        return proximo2