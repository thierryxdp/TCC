# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    qtd_palavra = 1
    dicionario = {}
    list_elem = frases.split()
    for i in range(len(list_elem)):
        if list_elem.count(list_elem[i]) > 1:
            qtd_palavra = qtd_palavra*list_elem.count(list_elem[i])
        dicionario[list_elem[i]] = qtd_palavra
        return dicionario