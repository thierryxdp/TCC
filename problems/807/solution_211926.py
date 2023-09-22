def conta_frases(frase):
    split1=str.join('/',str.split(frase,"."))
    split2=str.join('/',str.split(split1,"!"))
    split3=str.join('/',str.split(split2,"..."))
    split4=str.join('/',str.split(split3,"?"))
    splitfinal=str.split(split4,"/")
    splitfinal=filter(None,splitfinal)
    return len(splitfinal)