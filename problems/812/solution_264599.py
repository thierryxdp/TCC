def retira_pontuacao(frase):
    
    trave = str.strip(frase, str.split(frase, "-"))
    virg = str.strip(frase, str.split(frase, ","))
    doisp = str.strip(frase, str.split(frase, ":"))
    pontovirg = str.strip(frase, str.split(frase, ";"))
    pontofim = str.strip(frase, str.split(frase, "."))
    
    return virg, doisp, pontovirg, pontofim