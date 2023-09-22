# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    frase = frase.split()
    result={}
    for palavra in frase:
        result.update({palavra:frase.count(palavra)})
    return result