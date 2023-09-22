# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """retorna um dict contendo cada palavra da frase como chave, e como valor quantas vezes a palavra aparece;
    str -> dict"""
    l=str.split(frase)
    d={}
    for x in l:
        d[x]=list.count(l,x)
    return d