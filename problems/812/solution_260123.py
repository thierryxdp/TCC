def retira_pontuacao(frase):
    
    nfrase = frase.replace(".", " ")
    nfrase = nfrase.replace(",", " ")
    nfrase = nfrase.replace("!", " ")
    nfrase = nfrase.replace("?", " ")
    nfrase = nfrase.replace("...", " ")
    nfrase = nfrase.replace("-", " ")
    nfrase = nfrase.replace(";", " ")
    
    return(nfrase)