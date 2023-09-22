# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''Função que recebe um string (frase) como entrada e retorna
    um dicionário onde cada palavra dessa string é uma chave e tem
    como valor o número de vezes que a palavra aparece; str->dict'''
    palavras= str.split(frase,' ')
    resultado={}
    for i in palavras:
        if i not in resultado:
            resultado[i]=1
        else:
            resultado[i]+=1
    return resultado