def retira_pontuacao (frase):
    '''
    funcao que recebe uma frase e retorna outra frase que 
    retira todos os tipos de pontuacao e substitui por espaço
    '''
    
    um = str.replace(frase,'-',' ')
    dois = str.replace(um,',',' ') 
    tres = str.replace(dois,':',' ')
    quatro = str.replace(tres,';',' ')
    cinco = str.replace(quatro,'.',' ')
    seis = str.replace(cinco,'?',' ')
    final = str.replace(seis,'!',' ')
    
    return final