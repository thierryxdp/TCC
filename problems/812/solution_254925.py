def retira_pontuacao(frase):
    '''funcao que dada uma frase retorne outra frase na ordem in versa sem letras maisculas e sem elementos depontuacao;str-->str'''
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    return frase