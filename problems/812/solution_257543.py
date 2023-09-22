def eh_ponto(caractere):
    if caractere in '_,:;.!?':
        return ''
    else:
        return caractere

    
def retira_pontuacao(frase):
    return str.join('',map(eh_ponto,frase))