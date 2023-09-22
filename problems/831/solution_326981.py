def lingua_p(p):
    p=p.lower()
    vogais="aeiouáéíóúãõ"
    for i in p:
        if i in vogais:
            p=p.replace(i,i+"p"+i)
            vogais=vogais.replace(i,"x")
    return p