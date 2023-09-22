# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(l,p):
    ''' retorna o valor das lista das compras baseado no dicionario dos produtos.
    l= lista de compras 
    p=produtos
    list,dicionario -> int'''
    i=0
    s=0
    while i < len(l):
        chave=l[i]
        s=s+p[chave]
        i+=1
    return round(s,2)