# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(s):
    ''' recebe uma string e retorna um dicionario com as palavras e o numero de vezes que ela apareceu.
    s=str
    str-> dicionarios'''
    g=str.split(s)
    i=0
    d={}
    while i < len(g):       
        f=list.count(g,g[i])
        t={g[i]:f}
        d[g[i]]=f
        i+=1
        
    return d