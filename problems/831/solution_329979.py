def lingua_p(palavra):
    result = ''
    for i, letra in enumerate(self.__frase):
        result += letra
        if i < len(self.__frase) - 1 and letra == self.__frase[i + 1]:
            result += 'p'
    return result