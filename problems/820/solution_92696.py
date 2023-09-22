def posLetra(string, letra, ocorrencia):
    '''dada uma frase, retorna a posicao de dada ocorrencia de dada letra. caso a ocorrencia informada seja maior que o numero de ocorrencias totais, ira retornar -1
    str, str, int -> int'''
    cont_ocorrencia = 0
    ocorrencia_totais = str.count(string, letra)
    frase = []
    if ocorrencia > ocorrencia_totais:
        return -1
    else:
        for i in string:
            if i == letra:
                cont_ocorrencia += 1
                if cont_ocorrencia < ocorrencia:
                    list.append(frase, ' ')
                elif cont_ocorrencia >= ocorrencia:
                    list.append(frase, i)
            else:
                list.append(frase, i)
        return frase, list.index(frase, letra)