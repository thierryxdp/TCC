def retira_pontuacao(texto):
    """funcao que dada uma frase, retorna a frase com todos os pontos substituidos por espaco"""
    """str->str"""
    filtro1 = str.replace(texto,'-',' ')
    filtro2 = str.replace(filtro1,'.',' ')
    filtro3 = str.replace(filtro2,',',' ')
    filtro4 = str.replace(filtro3,'!',' ')
    filtro5 = str.replace(filtro4,'?',' ')
    return filtro5