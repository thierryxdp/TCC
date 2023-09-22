# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases): 
    res = {key: frases.count(key) for key in frases.split()}
    return res