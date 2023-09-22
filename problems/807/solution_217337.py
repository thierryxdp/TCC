def conta_frases(f):
    "str-->int"
    "Dada uma sentença, calcula o numero de frases que ela possuí"
    #O vódigo visa calcular essa sequencia trocando todos os pontos diferentes por o mais facil de ser analisado o "."
    #Depois de convetidos todos os outros pontos para o "."
    L1= str.replace(f,"?",".")
    L2= str.replace(L1,"!",".")
    L3= str.replace(L2,"...",".")
    L4= str.split(l3,".")
    return len(l4)