def freq_palavras(frases):
    '''função que recebe uma str(frases) e retorna um dict 
    onde cada palavra de frases é uma chave e o numero de ve
    zes que essa palvra aparece na str é o valor;str->dict'''
    frases=str.split(frases)
    resp=[]
    indice=0
    indice2=0
    for i in frases:
        if frases[indice] in frases:
            resp+=[frases[indice],list.count(frases,frases[indice])]
        indice+=1
            for var in range (0,(len(frases)):
                              if frases[indice2] in frases:
                              	rt+={frases[indice2]:list.count(frases,frases[indice2]),}
        indice2+=1
    return rt