def conta_frases(Texto):
    '''Função para definir quantas frases tem em determinado texto. As frases devem ser separadas pelas seguintes pontuaçoes: !/?/.../.'''
    String1 = Texto.replace('!','.')
    String2 = String1.replace('?','.')
    String3 = String2.replace('...','.')
    
   		return String3.count('.')