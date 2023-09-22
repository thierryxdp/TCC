def feq_palavras(frase):
    '''Essa função ao receber uma string ela retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece'''
    ''' str ->dic'''
    parte=str.split(frase)
    resultado={}
    for palavra in parte:
        um = list.count(parte,palavra)
        resultado[palavra]=um
        
    return resultado