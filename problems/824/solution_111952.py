# Dada uma frase, queremos
# retorná-la com as consoantes em maiúsculo.
# Resolução:
# 1. Define uma str vazia como a nova frase;
# 2. Uma vez que a função str.upper só vale para letras,
#    avalia se o i-ésimo elemento da frase não é vogal e, 
#    caso não seja, aplica a função;
# 3. Concatena todo i-ésimo elemento analisado à str de (1);
# 4. Repete o processo de i = 0 até i = tamanho da string menos 1
# 5. Devolve a nova string obtida concatenando os elementos.


def uppCons(frase: str) -> str:
    '''Dada uma frase, 
    retorna-a com as consoantes em maiúsculo'''
    novafrase = ''
    i = 0
    while (i < len(frase)):
        frase_elemento = frase[i]
        if (frase[i] not in 'aeiouáéíóúàôêõã'):
            frase_elemento = str.upper(frase[i])
        novafrase += frase_elemento
        i += 1
    return novafrase