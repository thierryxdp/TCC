def freq_palavras(frases):
    '''função que recebe uma str(frases) e retorna um dict 
    onde cada palavra de frases é uma chave e o numero de ve
    zes que essa palvra aparece na str é o valor;str->dict'''
    frases=str.split(frases)
    indice=0
    for i in frases:
        if frases[indice] in frases:
            resp={frases[indice]:list.count(frase,frases[indice]);}
        indice+=1
    return resp