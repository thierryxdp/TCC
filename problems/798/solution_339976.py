# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionario onde cada palavra dessa string é uma chave e tenha como valor o número de vvezes que a palavra aparece'''
    
    x=frases.split(' ')
    dicionario={}
    for i in x:
        dicionario[i]=x.count(i)
    return dicionario