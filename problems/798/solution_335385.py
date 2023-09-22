from collections import Counter
def freq_palaras(frases):
    lista=frases.list
    args=[]
    for i in lista:
        args.append(i)
    comtador = Counter(args)
    return contador