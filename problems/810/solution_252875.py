def inverte(frase):
        for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase, ponto , " ")