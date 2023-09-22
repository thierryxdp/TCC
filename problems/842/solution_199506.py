def pontos_por_time(lista):
    """
    """
    jogo1=lista[0]
    jogo2=lista[1]
    valor_jogo1=jogo1[2]
    valor_jogo2=jogo2[2]
    dicionario={jogo1[0]:0, jogo1[1]:0}
    vitoria_time1=valor_jogo1[0]>valor_jogo1[1]
    vitoria_time2=valor_jogo1[1]>valor_jogo1[0]
    vitoria_time1_2=valor_jogo2[0]>valor_jogo2[1]
    vitoria_time2_2=valor_jogo2[1]>valor_jogo2[0]
    empate= valor_jogo1[0]==valor_jogo2[1]
    empate_2= valor_jogo2[0]== valor_jogo2[1]
    #if vitoria_time1:
    #    dicionario[time1]+=3
    #else vitoria_time2:
    #    dicionario[time2]+=3
    #elif empate:
    #     dicionario[time1]+=1
    #elif empate:
    #    dicionario[time2]+=2
    
    return empate