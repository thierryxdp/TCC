def retira_pontuacao(frasepontuada):
    
    '''Função qque substitui os sinais de pontuacao 
    por espaço.
    :param frasepontuada:str
    :return:str'''
    
    frase_n_pontuada=frasepontuada.replace("-"," ")
    frase_n_pontuada=frasepontuada.replace(","," ")
    frase_n_pontuada=frasepontuada.replace(':',' ')
    frase_n_pontuada=frasepontuada.replace(';',' ')
    frase_n_pontuada=frasepontuada.replace('.',' ')
    frase_n_pontuada=frasepontuada.replace('!',' ')
    frase_n_pontuada=frasepontuada.replace('?',' ')
    
    return frase_n_pontuada