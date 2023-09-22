# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    """Recebe uma string e verifica cada palavra e retorna um dict com as palvras e quantas vezes aparece.
    string -> dict"""

    separado = frases.split()
    semrep = []
    dicionario = {}

    for i in separado:
        if i not in semrep:
            semrep.append(i)
            dicionario[i] = frases.count(i)
    
    return dicionario