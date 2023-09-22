# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''Esta e a funcao que recebe uma string e retorna um dicionario onde
cada palavra dessa string e uma chave e tem como valor o numero de vezes
que a palavra aparece'''
    lista1=[]
    i=0
    for palavra in frase:
        lista1.append(frase.split())
        a = lista1.count(palavra)
    return {lista1}