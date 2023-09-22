def freq_palavras( frase ) :
    """Função que recebe como parâmetro uma string e retorna um dicionário contendo a as palavras dessa string co a chave que representa a quantudade de vezes que essa palavra apareceu. Entrada - > str; Saída -> dict"""
    dicionario = {}
    palavras = frase.split ( )
    for palavra in palavras :
        if palavra in dicionario.keys ( ) :
            dicionario [ palavra ] += 1
        if palavra not in dicionario.keys ( ) :
            dicionario [ palavra ] = 1
    return dicionario