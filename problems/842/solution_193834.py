def pontos_por_time(jogo_ida,jogo_volta):
    '''list->dict'''
    '''dada uma lista de 2 elementos, retorna um dicionario cujos mapeamentos sao nome do time -> nmr de pontos'''
    
    nome_t1 = jogo_ida[0]
    nome_t2 = joga_volta[0]
    
    if jogo_ida[2]>jogo_ida[3]:
        return vitoriat1
    elif jogo_ida[2]==jogo_ida[3]:
        return empate
    elif jogo_ida[2]<jogo_ida[3]:
        return derrotat1
    
    if jogo_volta[2]>jogo_volta[3]:
        return vitoriat1
    elif jogo_volta[2]==jogo_volta[3]:
        return empate
    elif jogo_volta[2]<jogo_volta[3]:
        return derrotat1
    
vitoriat1 = 3
empate = 1
derrotat1 = 0