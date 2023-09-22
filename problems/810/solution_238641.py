def inverte(frase):
    """Função que retorna uma frase inversa com as mesmas palavas da frase de entrada sem os caracteres e sem letras maiusculas.
    parametros:lista->str"""
    troca1 = str.replace(frase,'-',' ')
    troca2 = str.replace(troca1,',',' ')
    troca3 = str.replace(troca2,':',' ')
    troca4 = str.replace(troca3,';',' ')
    troca5 = str.replace(troca4,'?',' ')
    troca6 = str.replace(troca5,'!',' ')
    troca7 = str.replace(troca6,'.',' ')
    minuscula = str.lower(troca7)
    lista_P = str.split(minuscula)
    lista_I = lista_P[::-1]
    return str.join(' ', lista_I)