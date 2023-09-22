def conta_frases(sti):
    fra= str.replace(sti,'...','1')
    qua= fra.count('.')+fra.count('1')+fra.count('?')+fra.count('!')
    return qua