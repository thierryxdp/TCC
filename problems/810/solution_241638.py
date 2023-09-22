def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."
    fraseAlterada1 = frase.lower(frase)
    fraseAlterada2 = str.split(fraseAlterada1,('.',',','-','!','?',';',':','...'))
    fraseInvertida = fraseAlterada2.join(::-1)
    
    return fraseInvertida