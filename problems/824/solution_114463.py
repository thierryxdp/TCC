def uppCons(fra):
    cons='bcdfghjklmnpqrstvwxzç'
    frase=''
    i=0
    while i<len(fra):
        if fra[i] in cons:
            frase=frase+fra[i].upper()
            i=i+1
        return frase


#não pode aconteccer. entendeu? meu microfone nao está pegando