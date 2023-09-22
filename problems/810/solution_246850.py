def inverte (frase):
    '''dada uma frase, ele le a frase de tras pra frente
    sem nenhum tipo de carcter que não seja alfanumerico
    e poe tudo minusculo'''
    '''str->str'''

    if "-" in frase:

        frase= str.replace(frase, "-"," ")

    if "," in frase:

        frase= str.replace (frase, ",", " ") 

    if ":" in frase:
        frase= str.replace(frase, ":", " ")

    if ":" in frase:
        frase= str.replace(frase, ";", "")
    if "." in frase:
        frase= str.replace(frase, ".",")
    if "_" in frase:

        frase= str.replace (frase, "-", " ") 
    if "?" in frase:

        frase= str.replace(frase, "?"," ")

    if "!" in frase:
        frase= str.replace(frase, "!"," ")

    a=str.lower(frase)
    b=a.split(" ")

    c=b[::-1]
        
    d=str.join(" ",c)
	
    e=str.strip(d," ")
                           
    return str.replace(e,"  "," ")