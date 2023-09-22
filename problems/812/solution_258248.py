def retira_pontuacao (texto):
    '''sadf'''
    texto_semtravessao= str.replace(texto,'-',' ')
    texto_semvirgula= str.replace(texto_semtravessao,',',' ')
    texto_semdoispontos= str.replace(texto_semvirgula,':',' ')
    texto_semponto= str.replace(texto_semdoispontos,'.',' ')
    return texto_semponto