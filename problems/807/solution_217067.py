def conta_frases(texto):
    lista = texto.split()
    a=0
    for i in range(len(lista)):
        if lista[i]==". ":
            a+=1
        elif lista[i]=="...":
            a+=1
        elif lista[i]=="!":
            a+=1
        elif lista[i]=="?":
            a+=1
    return a