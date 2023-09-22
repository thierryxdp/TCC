# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def remove(s):
    pontuacao = ". ? !"
    for p in pontuacao:
        s = s.replace(p, " ")
    return s

def quant_palavras(frase):
 	s = remove(s)
    lista = frase.split()
    return len(lista)