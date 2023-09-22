# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
import string
def quant_palavras(frase):
    """Dada uma frase, retorna o número de palavras da frase.
    Assinatura: string-->int
    Teste:
    quant_palavras('Foi pelas festas da Coroação.')= 5
    quant_palavras('Eram de vária espécie, explicáveis e inexplicáveis, assim úteis como inúteis, umas graves, outras frívolas; gostava de saber tudo.')=19
    """
 
    frases=frase.split()
    return len(frases)