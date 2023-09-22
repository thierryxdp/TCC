def retira_pontuacao(frase):
    
    virg = str.join(" ",str.split(frase, ","))
    doisp = str.join(" ", str.split(frase, ":"))
    pontovirg = str.join(" ", str.split(frase, ";"))
    pontofim = str.join(" ", str.split(frase, "."))
    
    return virg, doisp, pontovirg, pontofim