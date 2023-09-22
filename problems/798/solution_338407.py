def freq_palavras(texto):
    lista =str.split(texto)
    repeticoes={}
    for palavra in lista:
        repeticao = list.count(lista,palavra)
        repeticoes[palavra]=repeticao
    return repeticoes# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis