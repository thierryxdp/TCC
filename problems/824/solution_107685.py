def uppCons(frase):
    answer = ""
    for letra in frase:
        if letra not in "aeiouAEIOU":
            answer = answer + letra.upper()
        else:
            answer = answer + letra
    return answer


print(uppCons(input("Enter a frase: ")))