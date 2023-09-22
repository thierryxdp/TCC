def retira_pontuacao(txt):
    '''Função que recebe uma string e retorna uma nova string retirado todo os 
    caracteres de pontuação; str -> str'''
    txt = str.replace(txt, ".", " ")
    txt = str.replace(txt, ",", " ")
    txt = str.replace(txt, "/", " ")
    txt = str.replace(txt, ":", " ")
    txt = str.replace(txt, "-", " ")
    txt = str.replace(txt, "_", " ")
    txt = str.replace(txt, ";", " ")
    
    return txt