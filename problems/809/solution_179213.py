# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    
    def alternate_comb(first:list, second:list)->list:
        assert len(first) == len(second) 
        
        n = len(first)
        combined = [1]
        
        for i in range(n):
            combined.append(first[i])
            combined.append(second[i])
            
        return combined