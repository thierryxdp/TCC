def carros(numeropessoas):
    """Função que retorna a quantidade necessária de carros para uma viagem, dado como parâmetro a quantidade de pessoas. Entrada -> int; Saída -> in"""
    capacidade = 5
    if (numeropessoas) >= capacidade:
        return numeropessoas//capacidade