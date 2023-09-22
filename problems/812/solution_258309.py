def retira_pontuacao(frase):
    '''Retorna toda a pontuação como espaço
    str -> str'''
    excl = frase.replace("!"," ")
    inte = excl.replace("?"," ")
    virg = inte.replace(","," ")
    trav = virg.replace("-"," ")
    pont = trav.replace("."," ")
    return pont