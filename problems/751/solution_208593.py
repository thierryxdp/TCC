# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna a quantidade de palavras de uma frase; recebe
    como parâmetro uma frase dada pelo usuário.String-->Int"""
    if((frase[0]==' ' and frase[len(frase)-1]!=' ') or (frase[0]!=' ' and frase[len(frase)-1]==' ')):
		return str.count(frase,' ')
    elif((frase[0]==' ' and frase[len(frase)-1]==' '):
        return str.count(frase,' ')-1
    else:
         return str.count(frase,' ')+1