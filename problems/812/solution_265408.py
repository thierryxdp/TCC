def retira_pontuacao (frase):
    """ Função que dada a frase, retira todos os caracteres 
    de pontuação e substitui por espaço.
    Entrada: string
    Saída : string"""
    x = str.replace(frase,'.' , ' ')
    y = str.replace(x,',', ' ')
    z = str.replace(y,'!', ' ')
    t = str.replace(z,'-', ' ')
    i = str.replace(t,'?', ' ')
    return  i