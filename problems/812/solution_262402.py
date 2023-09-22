retira_pontuacao(frase):
   	nayara = frase.replace("-", " ")
    nayara = nayara.replace(",", " ")
    nayara = nayara.replace(":", " ")
    nayara = nayara.replace(";", " ")
    nayara = nayara.replace("...", " ")
    nayara = nayara.replace("!", " ")
    nayara = nayara.replace("?", " ")
    nayara = nayara.replace(".", " ")
    
    return frase