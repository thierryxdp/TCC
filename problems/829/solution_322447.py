def soma_h(termos):
    "Função que retorna o valor de H sendo H=1+1/2+...+1/N, onde N é o número de termos dado de entrada. int --> float"
    soma=1
    for n in range(2,termos+1):
        soma+=1/n
    return round(soma,2)