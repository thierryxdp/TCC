def retira_pontuacao(frase):
    """
    Códoigo que retorna uma determinada string substituindo
    pontuação por espaço.
    :entrada --> string:
    :return --> string
    """
    z2='-',',',':',';','.'
    frase1= frase.replace('.', ' ')        
    return frase1