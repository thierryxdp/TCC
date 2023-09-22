def uppCons(fra):
    cons='bcdfghjklmnpqrstvwxz'
    
    i=0
    while i<len(fra):
        if fra[i] in cons:
            fra=fra.replace(fra[i],fra[i].upper())
        i=i+1
    return fra

resultado=uppCons('oi, eu sou o jair.')
print(resultado)