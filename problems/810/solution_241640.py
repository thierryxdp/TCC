def inverte(frase:str)->str:
    "Dada uma frase, retorna ela invertida."
    frase = frase[]
    fraseAlterada1 = frase.lower(frase)
    fraseAlterada2 = str.split(fraseAlterada1,('.',',','-','!','?',';',':','...'))
   
    return fraseAlterada2