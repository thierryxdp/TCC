def conta_frases(f):
    "str-->int"
    "Dada uma sentença, calcula o numero de frases que ela possuí"
    #O código troca todos os pontos para um mais identificavel(neste caso o ponto final), depois separa as frases distintas pelo "." e retorna o numero de componentes na lista -1(este fator é devido a não ter nada depois do ultimo ponto final da frase)
    L1= str.replace(f,"?",".")
    L2= str.replace(L1,"!",".")
    L3= str.replace(L2,"...",".")
    L4= str.split(L3,".")
    return len(L4)-1