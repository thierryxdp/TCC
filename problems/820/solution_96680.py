def posLetra(frase,let,ocor):
    """Funcao calcula e retorna uma string com a ocorrencia(pos) de uma letra(let) 
    str,str-->ind"""
    pos=0
    ocorrenciaatual=0
    while ocorrenciaatual<len(lista):
        if let in frase[pos+1:]:
            pos=frase.index(let,pos)
            ocorrenciaatual=ocorrenciaatual+1
        else:
            return -1
    return pos