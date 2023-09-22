def hashtag(s):
#A entra será uma palavra (s). Defini este mesmo (s) de (string) como
#Minha variavel, inclui um "#" que entrara no inicio
#Somei com a indexaçao da palavra, o comenado len contou em quanto
#Ficaria a metade desta string, por isso o len(s)//2 e por fim coloquei
#A "#" no fim e meu retoro é este que esta ecrito abaixo.
    """Função recebe uma str e insere o caractere ”#” no inıcio, 
    meio efinal; str-> str"""
    s = "#" + s[ : len(s)//2] + "#" + s[len(s)//2 : ] + "#"
    return s