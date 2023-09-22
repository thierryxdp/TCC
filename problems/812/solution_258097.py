def retira_pontuacao(frase):
    ''''Dado uma frase, retorna uma frase sem nenhuma pontuação com espaços
    em seu lugar.str -> str'''
    frase = str.strip(frase,'!')
    frase = str.strip(frase,'?')
    frase = str.strip(frase,'...')
    frase = str.strip(frase,'.')
    frase = str.strip(frase,'-')
    frase = str.strip(frase,',')
    frase = str.strip(frase,':')
    frase = str.strip(frase,';')
     
    return frase