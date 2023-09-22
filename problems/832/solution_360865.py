def eh_quadrada(Bola_do_Quico):
    '''Função que retorna se uma matriz é quadrada
    list -> bool'''
    if len(Bola_do_Quico)==0:
        return True 
    elif len(Bola_do_Quico)==len(Bola_do_Quico[0]):
        return True 
    else:
        return False
    #sim