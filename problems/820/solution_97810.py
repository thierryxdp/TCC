def posLetra(frase,let,ocor):
    """Funcao calcula e retorna uma string com a ocorrencia(ocor) de uma letra(let) 
    str,str,ind-->ind"""
    pos=0
    ocor_atual=0
    while ocor_atual<ocor:
        if let in frase[pos:]:
            pos=frase.index(let,pos)
            ocor_atual=ocor_atual+1
            pos=pos+1
        else:
            return -1
    return pos-1