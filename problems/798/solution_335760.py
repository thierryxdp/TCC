def freq_palavras(frase):
    """função que retorna um dicionário com a palavra como chave e o numero de vezes que ela aparece como valor
    str->dict"""
    repet={}
    for palavras in str.split(frase):
        repet[palavras]= list.count(str.split(frase),palavras)
        return repet