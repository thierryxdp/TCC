# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(string):
    '''função que conta as palavras e adiciona suas 
    frequências em um dicionário.
    str->dict'''
    a={}
    separado=string.split(' ')
    for i in range(len(separado)):
        if separado[i] not in a:
            a[separado[i]]=1
        else:
            a[separado[i]]=a[separado[i]]+1
       
    return a