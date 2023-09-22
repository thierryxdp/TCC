def retira_pontuacao(frase):
    virg = str.replace(frase,","," ")
    doisp = str.replace(frase,":"," ")
    pontovirg = str.replace(frase,";"," ")
    pontofim = str.replace(frase,"."," ")
    
    return virg, doisp, pontovirg, pontofim