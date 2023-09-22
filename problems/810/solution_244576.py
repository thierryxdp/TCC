def inverte(frase):
    novo1 = frase.replace("-", " ")
    novo2 = novo1.replace(",", " ")
    novo3 = novo2.replace(":", " ")
    novo4 = novo3.replace(";", " ")
    novo5 = novo4.replace(".", " ")
    novo6 = novo5.replace("?", " ")
    novo7 = novo6.replace("!", " ")
    novo8 = novo7.replace("...", " ")
    
    nova_frase = novo8.lower()
    nova_frase2 = nova_frase.split
    
    return list.reverse(nova_frase)