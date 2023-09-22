# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Essa função, dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2. 
        
        Parameters:
            lista1 = primeira lista a ser inserida. Deve ter len = 3
            lista2 = segunda lista a ser inserida. Deve ter len = 3

        Testes:
            intercala([1, 3, 5], [2, 4, 6]) = [1, 2, 3, 4, 5, 6]
            intercala('As curiosidades de Capitu dão para um capítulo. Eram de vária espécie, explicáveis e inexplicáveis, assim úteis como inúteis, umas graves, outras frívolas; gostava de saber tudo.') = 2
            intercala('No colégio onde, desde os sete anos, aprendera a ler, escrever e contar, francês, doutrina e obras de agulha, não aprendeu, por exemplo, a fazer renda; por isso mesmo, quis que prima Justina lhe ensinasse. Se não estudou latim com o Padre Cabral foi porque o padre, depois de lhe propor gracejando, acabou dizendo que latim não era língua de meninas. Capitu confessou-me um dia que esta razão acendeu nela o desejo de o saber. Em compensação, quis aprender inglês com um velho professor amigo do pai e parceiro deste ao solo, mas não foi adiante.') = 4

        Returns:
            uma lista L3 que é formada intercalando os elementos de L1 e L2.
            list, list --> list
    """
    lista = lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]
    return lista