# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
 '''a função retorna o número de frases que 
    existe em um determinado texto
    entrada:str
    saída:int'''
     x = str.replace(frase,'...','@')
    return str.count(x,'.')+str.count(x,'!')+str.count(x,'?')+str.count(x,'@')