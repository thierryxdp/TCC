def inverte(frase):
    ''' essa funcao retorna a frase dada na entrada invertida '''
    frase1 = substituir(frase)
    semMaiuscula = str.lower(frase1)
    listaDaFrase = str.split(semMaiuscula)
    listainvertida = (listaDaFrase[::-1])
    final = str.join(' ',listainvertida)
    return final