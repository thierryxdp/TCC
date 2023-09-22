def carros(pessoas,vaga=5):
    """Essa função calcula a quantidade de carros necessarios para uma viagem.
    Recebe números de pessoas e quantidade de vagas.
    Retorna quantidade de carros necessarios."""
    return max(pessoas/vagas) 
#Essa função calcula o valor das raízes reais, recebendo os parâmetros a, b e c, usando duas equações e chamando duas das funções anteriores.
#int,int,int → int