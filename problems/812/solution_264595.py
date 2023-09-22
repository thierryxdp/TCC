def retira_pontuacao(frase):
    virg = str.split(frase,","," ")
    doisp = str.split(frase,":"," ")
    pontovirg = str.split(frase,";"," ")
    pontofim = str.split(frase,"."," ")
    
    return virg, doisp, pontovirg, pontofim