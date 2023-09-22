# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    ''' retorna o numero de vezes que uma palavra aparece, str->int'''
    dicionario={}
    frase1=str.split(frases)
    for palavra in frase1:
        dicionario[palavra]=frase1.count(palavra)
    return dicionario