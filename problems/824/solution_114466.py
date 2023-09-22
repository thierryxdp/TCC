def uppCons(fra):
    cons='bcdfghjklmnpqrstvwxzç'
    
    i=0
    while i<len(fra):
        if fra[i] in cons:
            fra=fra.replace(fra[i],fra[i].upper())
        i=i+1
    return fra