def retira_pontuacao(frasepontuada):
    
    '''Função qque substitui os sinais de pontuacao 
    por espaço.
    :param frasepontuada:str
    :return:str'''
    
    frasepontuada=frasepontuada.replace('-',' ')
    frasepontuada=frasepontuada.replace(',',' ')
    frasepontuada=frasepontuada.replace(':',' ')
    frasepontuada=frasepontuada.replace(';',' ')
    frasepontuada=frasepontuada.replace('.',' ')
    frasepontuada=frasepontuada.replace('!',' ')
    frasepontuada=frasepontuada.replace('?',' ')
    
    return frasepontuada