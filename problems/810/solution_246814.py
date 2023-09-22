def inverte (frase):

it "I" in frase:

frase= str.replace (frase, "-"," ")

if "," in frase:

frase= str.replace (frase, ",", " ") if ":" in frase:

frase= str.replace(frase, ":", " ") if ":" in frase: frase= str.replace

(frase, ";", "") if "." in frase:

frase= str.replace (frase, "."," if "_" in frase:

frase= str.replace (frase, "-", " ") 17 "?" in frase:

frase= str.replace (frase, "?"," ")

if "I" in frase: frase= str.replace (frase, "!"," ")

a-str.lower (frase) b= a.split(" ")

cmb [::-1] d=str.join(" ", c)

e-str.strip (d," ")

return str.replace(e,"