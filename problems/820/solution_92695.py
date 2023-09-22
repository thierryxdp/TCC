def posLetra(string, letra, ocorrencia):
    '''dada uma frase, retorna a posicao de dada ocorrencia de dada letra. caso a ocorrencia informada seja maior que o numero de ocorrencias totais, ira retornar -1
    str, str, int -> int'''
    cont_ocorrencia = str.count(string, letra)
    frase = []
    if ocorrencia > cont_ocorrencia:
        return -1
    else:
        for i in string:
            if i == letra:
                if cont_ocorrencia < ocorrencia:
                    list.append(frase, ' ')
                elif cont_ocorrencia >= ocorrencia:
                    list.append(frase, i)
            else:
                list.append(frase, i)
        return list.index(frase, letra)