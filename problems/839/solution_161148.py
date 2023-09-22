def carros(numbers, vagas):
    if numbers%vagas ==0:
        return numbers/vagas
    else:
        return numbers//vagas + 1