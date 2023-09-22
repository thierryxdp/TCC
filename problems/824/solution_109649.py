def uppCons(phrase):
    answer = ""
    i = 0
    while i < len(phrase):
        if phrase[i] not in "aãeéêiíoóôõuúûAEIOU":
            answer = answer + phrase[i].upper()
        else:
            answer = answer + phrase[i]
    return answer