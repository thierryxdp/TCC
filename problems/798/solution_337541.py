def freq_palavras(frases):
    texto=str.lower(frases)
    texto=str.split(frases," ")
    i=0
    dicio= {texto[0]:list.count(list(texto),texto[0])}
    while i<len(texto):
        dicio[texto[i]]=list.count(list(texto),texto[i])
        i=i+1
    return dicio# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis