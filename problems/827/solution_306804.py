def qtd_divisores(numero):
    """Função verifica para todo número de 1 até o número recebido
    (é escrito range(1,numero+1) pois a função range é excludente
    quanto o último número do intervalo rescebido), e verifica se o número
    recebido possui resto 0 quando dividido pelo do range, uma vez que,
    se o resto for 0, o número é divisor. Para cada divisor é adicionado
    em 1 uma variável que começa com o valor 0. Após verificar todos
    números, retorna o número da variável, que é o número de divisores.
	int-> int"""
    divisores=0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            divisores+=1
    return divisores