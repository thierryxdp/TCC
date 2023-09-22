def pontos_por_time (jogo_da_ida,jogo_da_volta):
    """Função que dada duas listas, que contem dois elementos que são listas representando o resultado de jogos de ida
e volta de dois times. Sendo vitória = 3 pontos, empate = 1 ponto e derrota = 0 pontos."""
    """Lista, Lista->Dicionario"""
    if jogo_da_ida[1][0]==jogo_da_ida[1][1] and jogo_da_volta[1][0]==jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:2,jogo_da_ida[0][1]:2}
    elif jogo_da_ida[1][0]==jogo_da_ida[1][1] and jogo_da_volta[1][0]>jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:1,jogo_da_ida[0][1]:4}
    elif jogo_da_ida[1][0]==jogo_da_ida[1][1] and jogo_da_volta[1][0]<jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:4,jogo_da_ida[0][1]:1}
    elif jogo_da_ida[1][0]>jogo_da_ida[1][1] and jogo_da_volta[1][0]==jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:4,jogo_da_ida[0][1]:1}
    elif jogo_da_ida[1][0]>jogo_da_ida[1][1] and jogo_da_volta[1][0]<jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:6,jogo_da_ida[0][1]:0}
    elif jogo_da_ida[1][0]>jogo_da_ida[1][1] and jogo_da_volta[1][0]>jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:3,jogo_da_ida[0][1]:3}
    elif jogo_da_ida[1][0]<jogo_da_ida[1][1] and jogo_da_volta[1][0]==jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:1,jogo_da_ida[0][1]:4}
    elif jogo_da_ida[1][0]<jogo_da_ida[1][1] and jogo_da_volta[1][0]<jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:3,jogo_da_ida[0][1]:3}
    elif jogo_da_ida[1][0]<jogo_da_ida[1][1] and jogo_da_volta[1][0]>jogo_da_volta[1][1]:
        tabela={jogo_da_ida[0][0]:0,jogo_da_ida[0][1]:6}
    return tabela