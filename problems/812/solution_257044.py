def retira_pontuacao(texto):
    """Substitui todos os caracteres de pontuacao por espaco 
    dado: um texto"""
    
    textoF=texto.replace('.', ' ')
    textoF=textoF.replace('!', ' ')
    textoF=textoF.replace('?', ' ')
    textoF=textoF.replace('-', ' ')
    textoF=textoF.replace(',', ' ')
    textoF=textoF.replace(':', ' ')
    textoF=textoF.replace(';', ' ')
    
    
    return textoF