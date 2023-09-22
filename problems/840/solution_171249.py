def bolos(xicaras=2,ovos=3,colheres=5):
    """Função que retorna a quantidade de bolos que se pode fazer dados o número de xícaras de farinha de trigo, ovos e colheres de sopa."""
  if xicaras<2 or ovos<3 or colheres<5:
        return 0
    else:
        return min((xicaras//2,ovos//3,colheres//5))