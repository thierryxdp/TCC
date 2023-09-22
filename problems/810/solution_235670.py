def retira_pontuacao(frase):
    '''uma função que substitui todos os caracteres de pontuação de uma frase por espaço
    str -> str'''
    nfrase  = str.replace(frase,"?"," ")
    mfrase  = str.replace(nfrase,"-"," ")
    bfrase  = str.replace(mfrase,","," ")
    dfrase  = str.replace(bfrase,":"," ")
    efrase  = str.replace(dfrase,";"," ")
    afrase  = str.replace(efrase,"."," ")
    AQUELAPowaDeFraseSEMPontuacao = str.replace(afrase,"!"," ")
    return AQUELAPowaDeFraseSEMPontuacao

def inverte(textinho):
    '''uma função que dada uma frase, retorna uma outra frase que contenha as mesmas
    palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem pontuação.
    str -> str'''
    MoFomeAi = str.lower(retira_pontuacao(textinho))
    queria comer um hamburguer = str.split(mo fome ai)
    tudo invertido nessa bosta como o problema pediu = queria comer um hamburguer[::-1] 
    return tudo invertido nessa bosta como o problema pediu