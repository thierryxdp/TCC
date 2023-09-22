# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''A função calcula o número
    de vezes que uma palavra aparece dentro de 'frases', no formato
    dicionário. Assinatura: str->dict.'''
    ls = frases.split()
    d={}
    for x in ls:
        i=0
        for y in ls:
            if x == y:
                i=i+1
        d[x]=i
    return d