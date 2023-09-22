def inverte (texto):
    ''' Função que recebe uma str contendo uma frase, e retorna a
    mesma invertida, sem as pontuações e sem letras maiúsculas
    str -> str '''
    
    subs1 = str.replace(texto,'-',' ')
    subs2 = str.replace(subs1,',',' ')
    subs3 = str.replace(subs2,'!',' ')
    subs4 = str.replace(subs3,'.',' ')
    subs5 = str.replace(subs4,'?',' ')
    subs6 = str.replace(subs5,':',' ')
    subs7 = str.replace(subs6,';',' ')
    
    sempontuacao =  str.split(subs7)
    list.reverse(sempontuacao)
    invertido = str.join(' ', sempontuacao)
    frase_alterada = str.lower(invertido)
    
    return frase_alterada