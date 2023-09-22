# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Dada uma frase, a função retorna o número de palavras presentes na frase.
        
        Parameters:
            frase = frase a ser inserida e avaliada

        Testes:
            SIGA(("Newton",7,8,10)) = ('Newton', 8.3, 'aprovado', 'Parabéns!')
            SIGA(("Newton",7,7,7)) = ('Newton', 7.0, 'aprovado', 'Parabéns!')
            SIGA(("João",7,5,5)) = ('João', 5.7, 'aprovado')
            SIGA(("João",5,5,5)) = ('João', 5.0, 'aprovado')
            SIGA(("Thiago",3,4,2)) = ('Thiago', 3.0, 'reprovado')

        Returns:
            número de palavras presentes na frase
            str --> int
    """
    lista = str.split(frase)
    numero = len(lista)
    return numero