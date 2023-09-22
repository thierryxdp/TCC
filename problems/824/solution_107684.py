def uppCons(frase):
    answer = ""
    for letter in frase:
        if letra not in "aeiouAEIOU":
            answer = answer + letra.upper()
        else:
            answer = answer + letre
    return answer


print(uppCons(input("Enter a frase: ")))