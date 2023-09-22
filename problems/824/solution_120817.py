#Função que recebe uma frase como entrada e retorna a frase com todas as suas consoantes em maiúsculo e os demais caractere na ordem original da frase; str = str
def consoante(frase):
    proximo = 0   
    while proximo < len(frase):
           if frase[proximo] in 'bcdfghjklmnpqrçstvywxz':
               frase = str.replace(frase,frase[proximo],str.upper(frase[proximo]))         
           proximo = proximo + 1
    return frase