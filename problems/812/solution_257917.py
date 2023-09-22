def retira_pontuacao(frase):
    """Função que retorna a frase onde todos os caracteres de pontuação sao substituidos
    por espaço, str-->str"""
    filtro1 = str.replace(frase,'-',' ')
    filtro2 = str.replace(filtro1,',',' ')
    filtro3 = str.replace(filtro2, '.',' ')
    filtro4= str.replace(filtro3, '?', ' ')
    filtro5= str.replace(filtro4, '!', ' ')
    filtro6= str.replace(filtro5, ':', ' ')
    filtro7=str.replace(filtro6, ';' , ' ')
    return filtro7