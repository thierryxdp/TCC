def posLetra(texto,letra,ocorrencia):
     quantOcorrencia = str.count(texto,letra)
     indiceLetra = 0
     resposta = []
     if quantOcorrencia < ocorrencia:
        return -1
     while indiceLetra < len(texto):
        if texto[indiceLetra] == letra:
            resposta.append(indiceLetra)
        indiceLetra = indiceLetra + 1
     return resposta[(ocorrencia-1)]