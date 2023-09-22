def feq_palavras(frases):
    '''Essa função ao receber uma string ela retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece'''
    ''' str ->dic'''
    parte= str.split (frases)
    final= {}
    for palavra in parte:
        um = list.count(parte,palavra)
        final[palavra]=um
        
        return final