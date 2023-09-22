def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."   
    lista = str.split(frase)
    lista.reverse()
    fraseAlterada1 = str.join(" ", lista)
    
    fraseAlterada2 = fraseAlterada1.replace('.',' ')
    fraseAlterada3 = fraseAlterada1.replace(',',' ')
    fraseAlterada4 = fraseAlterada1.replace('-',' ')
    fraseAlterada5 = fraseAlterada1.replace(':',' ')
    fraseAlterada6 = fraseAlterada1.replace(';',' ')
    fraseAlterada7 = fraseAlterada1.replace('!',' ')
    fraseAlterada8 = fraseAlterada1.replace('?',' ')
    fraseAlterada9 = fraseAlterada1.replace('...',' ')
    
    return fraseAlterada9



    
    return fraseInvertida