def conta_frases(texto):
    """Conta quantas frases temno texto; str ==> int"""
    quant= texto.split('...') 
    #print (quant)
    quant1= quant.count('')
    q= "".join(quant)
    #print (quant1)
    #print (q)
    quant2= q.count('?')
    #print (quant2)
    quant3= q.count('.')
    #print (quant3)
    quant4= q.count('!')
    #print (quant4)
    return quant1+quant2+quant3+quant4
#