def retira_pontuacao(frase):
    """retorna a frase substituindo os caracteres de pontuacao por espaco"""
    frase = str.replace(frase,',', '.')
    frase = str.replace(frase,'?', '.')
    frase = str.replace(frase,'!', '.')
    frase = str.replace(frase,'-', '.')
    frase = str.replace(frase,';', '.')
    frase = str.replace(frase,':', '.')
    return str.replace(frase, '.', ' ')