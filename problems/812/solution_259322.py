def caracter(c):
    pont=["!","?",";",":",".","...",",","-","  "]
    return " " if c in pont else c
def retira_pontuacao(texto:str)->str:
    "retira todas as pontuaçoes do texto"
    fraseA=str.join("",map(caracter,texto))
    return fraseA