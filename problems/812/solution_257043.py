def retira_pontuacao(texto):
    """Substitui todos os caracteres de pontuacao por espaco 
    dado: um texto"""
    
    textoF=texto.replace('.', ' ')
    textoF=texto.replace('!', ' ')
    textoF=texto.replace('?', ' ')
    textoF=texto.replace('-', ' ')
    textoF=texto.replace(',', ' ')
    textoF=texto.replace(':', ' ')
    textoF=texto.replace(';', ' ')
    
    
    return textoF