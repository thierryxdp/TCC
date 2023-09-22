def conta_frases(texto):
    quant= texto.count('...') 
#    print (quant)
    amor= texto.split('...')
    texto= ''.join(amor)
#    print (quant1)
   # print (quant2)
    quant3= texto.count('.')
 #   print (quant3)
    quant4= texto.count('!')
#    print (quant4)
    quant5 = texto.count(';')
 #   print(quant5)
    return quant+quant2+quant3+quant4+quant5