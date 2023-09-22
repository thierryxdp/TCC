frequencia de palavras
def freq_palavras(frase):
    '''função que dada uma frase retorna um dicionário onde cada palavra é uma chave e tenha como valor
    o número de vezes que a palavra se repete; str->dict'''
    dic={}
    frase = str.split(frase,' ')
    for letra in range(len(frase)):
        if frase[letra] in dic:
            dic[frase[letra]] += 1
        else:
            dic[frase[letra]] = 1
    return dic# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis