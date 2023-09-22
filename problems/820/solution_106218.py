def posLetra(frase, letra, numero):
    
    palavrass = list(frase)
    contador = 0
    ocorrencias = 0
    while len(palavrass) > contador:
        if letra in palavrass[contador]:
            ocorrencias += 1
            if ocorrencias == numero:
                return contador
            contador += 1
            if ocorrencias < numero:
                else:
                return ocorrencias