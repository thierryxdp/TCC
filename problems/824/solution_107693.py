def uppCons(frase):
    """Recebe como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas.
    str-->str"""
    frasedesejada=[]
    posicao=0
    while posicao<len(frase):
        if frase[posicao]!="a" and frase[posicao]!='e' and frase[posicao]!='i' and frase[posicao]!="o" and frase[posicao]!="u" and frase[posicao]!="á" and frase[posicao]!="é" and frase[posicao]!="í" and frase[posicao]!="ó" and frase[posicao]!="ú" and frase[posicao]!="ã":
            list.append(frasedesejada,str.upper(frase[posicao]))
        elif frase[posicao]=="a" or frase[posicao]=='e' or frase[posicao]=='i' or frase[posicao]=="o" or frase[posicao]=="u" or frase[posicao]=="á" or frase[posicao]=="é" or frase[posicao]=="í" or frase[posicao]=="ó" or frase[posicao]=="ú" or frase[posicao]=="ã":       
            list.append(frasedesejada,frase[posicao])
        posicao=posicao+1
    return str.join("",frasedesejada)