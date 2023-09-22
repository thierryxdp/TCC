def conta_frases(texto):
    """Essa função recebe um texto em string. Então é adcionado esse texto a outra string, porém com um espaço
    no final. dessa forma o proggrama reconhecerá a reticencias como um ponto, assim é retornado o numero de 
    frases
    stringg----->int"""
    texto2 = texto + " "
    return str.count(texto2, '! ')+str.count(texto2, '? ')+str.count(texto2, '. ')