def retira_pontuacao(frase):
    ''''Dado uma frase, retorna uma frase sem nenhuma pontuação com espaços
    em seu lugar.str -> str'''
    str.strip(frase,'!')
    str.strip(frase,'?')
    str.strip(frase,'...')
    str.strip(frase,'.')
    str.strip(frase,'-')
    str.strip(frase,',')
    str.strip(frase,':')
    str.strip(frase,';')
     
    return frase