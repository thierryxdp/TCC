# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "Função recebe uma frase e retorna palavras entre cada espaço"
    palavras = str.split(frase)
    return len(palavras)