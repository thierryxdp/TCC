def lingua_p(palavra):
    #palavra = list(palavra.lower())
    palavraNova = ''


    for i in list(range(len(palavra))):
        if palavra[i] in "aeiou":
            palavraNova = palavraNova + str(palavra[i]+ "p" + palavra[i])
        #    list.insert(palavra,i,str(palavra[i]+ "p" + palavra[i]))
        else:
            palavraNova = palavraNova + palavra[i]

    return palavraNova