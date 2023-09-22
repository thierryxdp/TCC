def retira_pontuacao (texto):
    '''sadf'''
    texto_semtravessao= str.replace(texto,'-',' ')
    texto_semvirgula= str.replace(texto_semtravessao,',',' ')
    texto_semdoispontos= str.replace(texto_semvirgula,':',' ')
    texto_semponto= str.replace(texto_semdoispontos,'.',' ')
    texto_semexclamacao= str.replace(texto_semponto,'!',' ')
    texto_seminterrogacao= str.replace(texto_semexclamacao,'?',' ')
    return texto_seminterrogacao