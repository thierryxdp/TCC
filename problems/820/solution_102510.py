def posLetra(frase, letra, ocorrencia):
    """dado uma frasee, uma letra e um numero indicando a ocorrencia, retorna a posicao da frase em que. str, str, int->int"""
    uso:posLetra(frase, letra, ocorrencia)
            Entrada:
            -frase(str): frase original
            -letra(str): letra especifica
            -ocorrencia(str,int):indica a ocorrencia
                
        saida:""" retorna a posicao que a string se enconta.(int)"""
            if frase.count(letra)<ocorrencia:
                return -1
            else:
                i=0
                letras=[]
                caracteres=list(frase)
                while i< len(caracteres) and len(letras)<ocorrencia:
                    if letra==caracteres[i]:
                        list.append(letras, caracteres[i])
                        i=i+1
                    return i-1