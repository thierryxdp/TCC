def inverte (frase):

    if "-" in frase:

        frase= str.replace (frase, "-"," ")

    if "," in frase:

        frase= str.replace (frase, ",", " ") 

    if ":" in frase:
        frase= str.replace(frase, ":", " ")

    if ":" in frase:
        frase= str.replace(frase, ";", "")
    if "." in frase:
        frase= str.replace (frase, ".",")
    if "_" in frase:

        frase= str.replace (frase, "-", " ") 
    if "?" in frase:

        frase= str.replace (frase, "?"," ")

    if "-" in frase:
        frase= str.replace (frase, "!"," ")

    	a-str.lower (frase)
    	b= a.split(" ")

    	c=b [::-1] d=str.join(" ", c)

    	e-str.strip (d," ")

    return str.replace(e,")