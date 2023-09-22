def retira_pontuacao(frase):
    resultado= str.strip(frase, '-')
    resultado= resultado + str.strip(frase,'.')
    resultado= resultado + str.strip(frase,',')
    resultado= resultado + str.strip(frase,':')
    resultado= resultado + str.strip(frase,';')
    resultado= resultado + str.strip(frase,'-')
    return resultado