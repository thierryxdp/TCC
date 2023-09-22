def melhor_volta (corrida):
    """
    Essa função define qual corredor teve a melhor volta
    da prova, o tempo e em qual volta foi.
    Parametro de entrada: list
    Valor de Retorno: tuple
    """
    melhores_voltas = []
    c_t_v = []
    
    for c in corrida:
        v = min (c)
        list.append(melhores_voltas,v)
    
    m_v = min(melhores_voltas)
    corredor = list.index(melhores_voltas,m_v)+1
    list.append (c_t_v, corredor)
    list.append (c_t_v, m_v)
    
        
    
    return c_t_v