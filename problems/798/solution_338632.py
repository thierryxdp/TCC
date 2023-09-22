# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas v
def freq_palavras(s):
    
    g=str.split(s)
    i=0
    d={}
    while i < len(g):       
        f=list.count(g,g[i])
        t={g[i]:f}
        d[g[i]]=f
        i+=1
        
    return d