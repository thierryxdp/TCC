def caracter(c):
    pont=["!","?",";",":",".","..."",","-","  "]
    retrun " " if c in pontuacpes else c
def retira_pontuacao(texto:str)->str:
    "retira todas as pontuaçoes do texto"
    fraseA=str.join(" ",map(caracter,frase)
    return fraseA