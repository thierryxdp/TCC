def inverte(frase):
  
    virgula=str.count(frase,",")
    travessao=str.count(frase,"/")
    Dois_p=str.count(frase,":")
    ponto=str.count(frase,".")
    inter=str.count(frase,"?")
    excla=str.count(frase,"!")
    ponto_virgula=str.count(frase,";")
    apos=str.count(frase,'-')
    if "," in frase:
        frase= frase.replace(',',' ',virgula)
    if "/" in frase:
        frase= frase.replace('/',' ',travessao)
    if ":" in frase:
        frase=frase.replace(':',' ',Dois_p)
    if "." in frase:
        frase= frase.replace('.',' ',ponto)
    if "?" in frase:
        frase= frase.replace('?',' ',inter)
    if "!" in frase:
        frase= frase.replace('!',' ',excla)
    if ";" in frase:
        frase= frase.replace(';',' ',ponto_virgula)
    if "-" in frase:
        frase= frase.replace('-',' ',apos)
    lista=[]
    lista[:]=frase
    lista=list.reverse(lista)
    lista2=join(lista)
    return lista2