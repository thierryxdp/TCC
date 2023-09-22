#Função que retira pontuações de uma string para contar quantas frases
#existem nela a aprtir dos espaços entre as frases, retornando o tamanho
#da lista em que foram armazenadas essas frases
#string -> int
def conta_frases(frase):
    x = str.replace(frase, "...", ".")
    x = str.replace(x, "?", ".")
    x = str.replace(x, "!", ".")
    x = str.split(x, ".")
    return len(x) - 1