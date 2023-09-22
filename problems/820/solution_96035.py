def posLetra(frase: str, letra: str, numero: int) -> int:
    """Dada uma frase, uma letra e um número, retorna em qual posição da frase
       a ocorrência (representada pelo número) da letra está

       Parameters:
       frase: Frase, na forma de string, onde será procurado
       letra: Letra, na forma de string, que será procurada
       numero: Número inteiro qualquer que representa o número da ocorrência

       Return:
       Dados os parâmetros "frase", "letra" e "numero", retorna a posição da
       ocorrência do parâmetro "letra" dentro do parâmetro "frase", no qual
       a ocorrência será representada pelo parâmetro "numero". Caso exista menos
       ocorrências da letra do que a ocorrência pedida, a função retorna -1

       Examples:
       posLetra("ababababa", "a", 4) == 6
       posLetra("ababababa", "a", 8) == -1
       posLetra("mariana come banana", "a", 3) == 6
    """

    quantidade = str.count(frase, letra)
    
    novo = str.replace(frase, letra, "@", (numero - 1))
    
    posicao = str.find(novo, letra)

    return posicao