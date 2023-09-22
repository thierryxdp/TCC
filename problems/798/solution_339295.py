#dado uma frase a função retorna um dicionário onde cada palavra
#dessa frase é um elemento do dicionário e sua respectiva chave 
# é o número de vezes que ela aparece
def freq_palavras(frase):
    frase2 = frase.split()
    frequencia = {}
    for x in frase2:
        if x in frequencia:
            frenquencia[x]+=1
        else:
            frequencia[x]=1
    return frequencia