def retira_pontuacao(frase):
    
    trave = str.strip(frase, "-")
    virg = str.strip(frase, ",")
    doisp = str.strip(frase, ":")
    pontovirg = str.strip(frase, ";")
    pontofim = str.strip(frase, ".")
    
    return virg + doisp + pontovirg + pontofim