def hashtag(s):
    """Essa função insere o caracter 3 no ínicio, no meio,e no final
    da string.Como entrada temos a string, e como saída temos a
    string modificada;
    str-> str"""
    tamanho=len(s)
    if tamanho==1:
        nova_string="#"+"#"+s+"#"
        return nova_string
    else:
        indice= int(len(s)/2)
        nova_s="#"+s[:1]+s[1:indice]+"#"+s[indice:]+"#"
        return nova_s