def bolos(A,B,C):
    '''Função que calcula o número, inteiro, máximo de bolos, pela receita,
    que podem ser feitos a partir dos ingredientes disponíveis
    
    	Parâmetros:
        	A - Quantidade de xícaras de farinha de trigo disponíveis
            B - Quantidade de ovos disponíveisc
            C - Quantidade de colheres de sopa de leite disponíveis
        
        Entradas: Int, Int, Int
        Saída: Int
        '''
    return min(A//2,B//3,C//5)