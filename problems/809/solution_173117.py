def intercala(first: list, second: list) -> list:
    assert len(first) == len(second)
 
    n = len(first)
    combined = []
 
    for i in range(n):
        combined.append(first[i])
        combined.append(second[i])
 
    return combined