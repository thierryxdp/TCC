def uppCons(frase):
    "Recebe uma frase e retorna ela com as consoantes em maiusculo:"
    "entrada: Str.  saida: Str"
    minusculo = 'bcçdfghjklmnpqrstvwxyz'         
    maiusculo = 'BCÇDFGHJKLMNPQRSTVWXYZ'         
    tabelaparasubstituicao = str.maketrans(minusculo,maiusculo) 
    return frase.translate(tabelaparasubstituicao)