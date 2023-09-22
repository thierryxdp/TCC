# Retira a pontuação
# periodo
# str->str
def retira_pontuacao(periodo):
    """Função que dada a str de entrada substitui a potuação por espaços"""
    """str->str"""
    return str.replace(periodo,","," ")+str.replace(periodo,"-","")+str.replace(periodo,":","")+str.replace(periodo,";","")+str.replace(periodo,".","")+str.replace(periodo,"!")+str.replace(periodo,"?","")+str.replace(periodo,"...","")