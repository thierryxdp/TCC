def melhor_volta (corrida):
    """
    Essa função define qual corredor teve a melhor volta
    da prova, o tempo e em qual volta foi.
    Parametro de entrada: list
    Valor de Retorno: tuple
    """
    melhores_voltas = []    
    c_t_v = []
    x = []
    
    for c in corrida:

        volta = c
        
        tempo = min (volta)
        
        v = list.index(volta,tempo)+1
        
        list.append(melhores_voltas,tempo)
        
        list.append(x,v)
    
    m_v = min(melhores_voltas)
    corredor = list.index(melhores_voltas,m_v)+1
    volta_perfeita = x[list.index(melhores_voltas,m_v)]
    list.append (c_t_v, corredor)
    list.append (c_t_v, m_v)
    list.append (c_t_v, volta_perfeita)
    
        
    
    return c_t_v