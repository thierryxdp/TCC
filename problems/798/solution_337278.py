# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(string):
    a={}
    separado=string.split(' ')
    for i in len(separado):
        if separado not in a:
            a[separado[i]]=1
        else:
            a[separado[i]]=a[separado[i]+1]
        i+=1
    return a