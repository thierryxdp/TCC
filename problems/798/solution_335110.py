# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''recebe uma string e retorna um dicionario onde cada palavra 
       dessa string e uma chave e tem como valor o numero de vezes
       que a palavra aparece
       str -> dict'''
    a=str.split(frases, ' ')
    b=0
    c={}
    
    while b<len(a):
        if a[b] in c:
            c[a[b]]=c[a[b]]+1
        else:
            c[a[b]]=1
    return c