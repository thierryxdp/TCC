def retira_pontuacao (texto):
    '''função que através do uso da da ferramento replace, remove
       todas as pontuações do texto
       string -> string'''
    texto_semtravessao= str.replace(texto,'-',' ')
    texto_semvirgula= str.replace(texto_semtravessao,',',' ')
    texto_semdoispontos= str.replace(texto_semvirgula,':',' ')
    texto_semponto= str.replace(texto_semdoispontos,'.',' ')
    texto_semexclamacao= str.replace(texto_semponto,'!',' ')
    texto_seminterrogacao= str.replace(texto_semexclamacao,'?',' ')
    return texto_seminterrogacao

def inverte (texto):
    '''DAS'''
    texto_sempontuacao= retira_pontuacao(texto)
    texto_em_string= str.split(texto_sempontuacao)
    texto_invertido= texto_em_string[len(texto_em_string):0:-1]
    return str.join('/',texto_invertido)