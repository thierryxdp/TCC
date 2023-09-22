# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(string):
    ''' Recebe uma string e retorna um dicionário
    com palavras e o numero de vezes que elas aparecem
    ent - string
    said - dic'''
    aux1=string.split()
    aux={}
    for x in aux1:
        if x in aux:
            aux[x]+=1
        else:
            aux[x]=1
    return aux