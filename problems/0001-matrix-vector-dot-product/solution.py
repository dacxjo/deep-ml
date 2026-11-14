def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.

    rows = len(a)
    cols = len(a[0])

    if cols != len(b):
        return -1

    result = []
    for i in range(len(a)):
        l = []
        for j in range(len(a[0])):
            l.append(a[i][j]*b[j])
        result.append(sum(l))
    return result
    