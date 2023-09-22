def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase
    substituida por espaço no local onde tinha
    pontuações (travessão, vírgula, dois pontos,
    ponto e vírgula, além da pontuação de encerramento de frase
    str -> str'''
    travessao = str.count(frase,"-")
    virgula = str.count(frase,",")
    dois_pontos = str.count(frase,":")
    ponto_e_virgula = str.count(frase,";")
    final = str.count(frase,".")
    exclam = str.count(frase,"!")
    retic = str.count(frase,"...")
    interr = str.count(frase,"?")
    if travessao!=0:
        return str.replace(frase,"-"," ",travessao)
    elif virgula!=0:
        return str.replace(frase,","," ",virgula)
    elif dois_pontos!=0:
        return str.replace(frase,":"," ",dois_pontos)
    elif ponto_e_virgula!=0:
        return str.replace(frase,";"," ",ponto_e_virgula)
    elif final!=0:
        return str.replace(frase,"."," ",final)
    elif exclam!=0:
        return str.replace(frase,"!"," ",exclam)
    elif retic!=0:
        return str.replace(frase,"..."," ",retic)
    elif interr!=0:
        return str.replace(frase,"?"," ",interr)
    else:
        return frase