def conta_frases(string):
    """Essa função retorna a quantidade de frases presentes na string 
    informada. Como entrada temos uma string e como saída temos o número
    de frases informadas dentro da mesma string;
    str-> int"""
    frase1=string.replace("...", " ")
    frase2=frase1.replace("?", " ")
    frase3= frase2.replace("!", " ")
    frase4=frase3.replace("."," ")
    numerodefrases=frase4.count(" ")
    return numerodefrases