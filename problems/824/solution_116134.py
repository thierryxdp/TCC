def uppCons(frase):
    "recebe como entrada uma frase (str) e retorna a frase com as consoantes maiúsculas (str)"
    posicao = 0
    frasenova = ""
    while posicao < len(frase):
        if frase[posicao] in ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]:
            frasenova = frasenova + str.replace(frase,frase[posicao],str.upper(frase[posicao]))
        else:
            frasenova = frasenova + frase[posicao]
        contador += 1
    return frasenova