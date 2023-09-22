def conta_frases(sti):
    fra= str.replace(sti,'...','1')
    qua= sti.count('.')+sti.count('1')+sti.count('?')+sti.count('!')
    return qua