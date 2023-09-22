def retira_pontuacao (frase):
    teste=frase.split("-")
    teste1=" ".join(teste)
    teste2=teste1.split(",")
    teste3=" ".join(teste2)
    teste4=teste3.split(":")
    teste5=" ".join(teste4)
    teste6=teste5.split(";")
    teste7=" ".join(teste6)
    teste8=teste7.split(".")
    teste9=" ".join(teste8)
    teste10=teste9.split("?")
    teste11=" ".join(teste10)
    teste12=teste11.split("!")
    teste13=" ".join(teste12)
    return teste13

def inverte (frase):
    """dada uma frase, retorna outra contendo as mesmas palavras na ordem inversa, sem pontuacao e letras maiusculas."""
    
    frase=retira_pontuacao(frase)
    frase=frase.lower()
    teste=frase.split(" ")
    teste=teste[::-1]
    frase=str.join(" ",teste)
    return frase