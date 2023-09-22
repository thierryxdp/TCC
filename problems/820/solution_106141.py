def posLetra(frase,letra,oco):
    'retorna quntas vezes a letra ocorre na frase'
    'string,string---int'
    rep=0
    x=0
    while x<len(frase):
        if frase[x].lower()==letra:
            rep+=1
        if rep==oco:
            resultado=x
            break
        x +=1
    return resultado