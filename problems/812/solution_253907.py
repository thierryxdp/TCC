#Questão 4
def retira_pontuacao(texto):
    """dada uma frase, troca topo tipo de pontuação por espaço(" ")
retornando a frase; ex: espaço('Leo.Leo,Leo) -> Leo Leo Leo
str -> str"""
    #Replace utilizado para fazer a troca de pontuação 
    return str.replace(str.replace(str.replace(str.replace(str.replace(texto,"."," "),":"," "),"-"," "),","," "),";"," ")