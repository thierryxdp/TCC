# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionario em que cada palavra da string 
    seja uma chave que tem como valor o número de vezes que a palavra aparece 
    str->dic'''
    div=frases.split(' ')
    dic={}
    for i in div:
        dic[i]=div.count(i)
    return dic