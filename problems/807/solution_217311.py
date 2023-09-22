def conta_frases(f):
    "str-->int"
    "Dada uma sentença, calcula o numero de frases que ela possuí"
    L1= str.replace(f,"?",".")
    L2= str.replace(L1,"!",".")
    L3= str.replace(L2,"...",".")
    L4= str.split((str.replace(L3," ",".")),"..")
    return len(L3)