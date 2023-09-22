def feq_palavras (frase):
    parte= str.split(frase)
    final= {}
    for palavra in parte:
        um = list.count(parte,palavra)
        final[palavra]=um
        
   return final