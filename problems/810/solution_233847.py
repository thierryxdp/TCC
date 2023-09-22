#Questão 5
def inverte(frase):
    """ função que dada uma frase retorna outra com as mesmas palavras,
    no entanto na ordem inversa, sem letras maiusculas e sem pontuação"""
    
    x = str.lower(frase)#utilizada para colocar as letras em minusculo
    # replace usado para trocar os pontos
    y = str.replace(str.replace(str.replace(str.replace(str.replace(x,".",""),",",""),"!",""),"-"," "),"?","")
    z = str.split(y," ")#utiliza split para separar a partir dos espaço 
    w = z[::-1] #apos estar em lista, coloca as palavras na ordem inversa
    

    return str.join(" ",w) # passa para str e coloca espaços