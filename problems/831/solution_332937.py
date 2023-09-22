def lingua_p(palavra):
    palavra_nova = ""
    for letra in palavra:
        if letra in "aeiouAEIOU":
            palavra_nova += "p" + letra + "p"
       	else:
            palavra_nova += letra
   	return palavra_nova.lower()