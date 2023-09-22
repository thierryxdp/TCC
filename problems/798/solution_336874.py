# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    """Recebe uma string e verifica cada palavra e retorna um dict com as palvras e quantas vezes aparece.
    string -> dict"""
    
    separado = frases.split()
    dicionario = {}
    cont = 0
    for i in separado:
        
        for j in separado:
        
            if i == j:
                cont += 1
        
        dicionario[i] = cont
        
        cont = 0
    return dicionario