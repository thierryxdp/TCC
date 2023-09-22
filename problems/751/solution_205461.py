# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Retorna a quantidade de palavras presentes na frase, string -> int """
    num_espacos = str.count(frase,' ');
    if(frase[0]==' ' or frase[-1]==' '):
        return num_espacos;
    else:
        if(frase[0]==' ' and frase[-1]==' '):
            return num_espacos-1;
        if (frase[0]!=' ' and frase[-1]!=' '):
            return num_espacos+1;