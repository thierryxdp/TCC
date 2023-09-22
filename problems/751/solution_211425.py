# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    lista=frase.split(' ')
    palavras= len(lista)
    if frase[0]==' ' and frase[-1]==' ':
        palavras= palavras-2
    if (frase [0]==' ' and frase[-1]!=' ') or (frase [0]!=' ' and 
                                                frase[-1]==' '):
        palavras= palavras-1
    return palavras