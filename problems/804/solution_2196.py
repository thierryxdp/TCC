def filtragem(valores):
    """calculo e retorno de uma tupla contendo aoenas os elementos pares"""
    valores_pares=()
    if valores[0]%2==0:
        valores_pares+=(valores[0],)
    if valores[1]%2==0:
        valores_pares+=(valores[1],)
    if valores[2]%2==0:
        valores_pares+=(numeros[2],)
    if valores[3]%2==0:
        valores_pares+=(valores[3],)
       return valores_pares