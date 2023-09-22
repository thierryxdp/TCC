def soma_h(n):
    """Função que ao receber um número, retorna
    a soma dos números anteriores,incluido o número passado,
    sendo que esse números são sempre
    os denominadores de 1;
    int -> float"""
    var=0
    for i in range(1,n+1):
        var+=1/i
    return round(var,2)