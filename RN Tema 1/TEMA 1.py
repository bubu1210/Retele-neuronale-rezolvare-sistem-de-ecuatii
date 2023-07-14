# cititre fisier
import sys
import numpy

file1 = open('sistemul1.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    print(line)
file1.close()

# parsarea coeficientilor
# print(Lines[0])
# print(Lines[1])
# print(Lines[2])
# print(len(Lines))
A = []
B = []


def parsare(line):
    line.strip()
    line = line.replace('+', '')
    line = line.replace('\n', '')
    coef = ['a', 'b', 'c']
    for index in range(len(coef)):
        if coef[index] not in line:
            A.append(0)
        elif line[0] == coef[index]:
            A.append(1)
            v = line.split(coef[index])
            line = v[1]
        elif line[0] == '-' and line[1] == coef[index]:
            v = line.split(coef[index])
            A.append(-1)
            line = v[1]
            # print(line)
        else:
            v = line.split(coef[index])
            A.append(int(v[0]))
            line = v[1]
            # print(line)
    if line[0] == '=':
        v = line.replace('=', '')
        B.append(int(v))

    # print(A)
    # print(B)


for line in Lines:
    parsare(line)
Matrix = []

A_np = A

def to_matrixA(A):
    m = []
    for i in range(0, len(A) // 3):
        elem = A[(i * 3):(i * 3 + 3)]
        Matrix.append(elem)
    print("Matricea A = ", Matrix)
    print("Matricea B = ", B)


to_matrixA(A)


# determinantul
# def determinant(Matrix):
#     Sarrus_Matrix = [Matrix[0], Matrix[1], Matrix[2], Matrix[0], Matrix[1]]
#     print(Sarrus_Matrix)
#     det = 0
#     p = 1
#     # diagonala principala
#     for i in range(0,3):
#         p = p * Sarrus_Matrix[i][i]
#     # print(p)
#     det = det + p
#     p = 1
#     # diagonala secundara
#     for i in range(0,3):
#         p = p * Sarrus_Matrix[i][2-i]
#     # print(p)
#     det = det + p
#
#     for i in range(1, len(Sarrus_Matrix)-2):
#         p = 1
#         for j in range(0, 3):
#             if i - 1 >= j:
#                 p = p * Sarrus_Matrix[i][j]
#         print(p)
#         det = det + p
#
#     print("Determinantul este:", det)


def determinantul(Matrix):
    # formula lui Leibniz
    det = Matrix[0][0] * (Matrix[1][1] * Matrix[2][2] - Matrix[1][2] * Matrix[2][1]) - Matrix[0][1] * (
                Matrix[1][0] * Matrix[2][2] - Matrix[2][0] * Matrix[1][2]) + Matrix[0][2] * (
                      Matrix[1][0] * Matrix[2][1] - Matrix[1][1] * Matrix[2][0])
    if det == 0:
        print("Determinantul este 0. Sistemul nu se poate rezolva momentan...")
        sys.exit()
    else:
        print("Determinnatul este diferit de 0 si este = ", det)
    return det


determinantul(Matrix)


def transpusa(Matrix):
    T = []
    for i in range(0, 3):
        t = []
        for j in range(0, 3):
            t.append(Matrix[j][i])
        T.append(t)
    print("Transpusa matricei este:", T)
    return T


T = transpusa(Matrix)


def minor_i_j(T, i, j):
    Minor = []
    for x in range(0, 3):
        minor = []
        for y in range(0, 3):
            if x != i and y != j:
                minor.append(T[x][y])
        if len(minor) != 0:
            Minor.append(minor)
    # print(Minor)
    return Minor


minor_i_j(T, 0, 1)


def adjuncta(T):
    Adjuncta = []
    for i in range(0, 3):
        adjuncta = []
        for j in range(0, 3):
            d = minor_i_j(T, i, j)
            d_i_j = pow(-1, i + j) * (d[0][0] * d[1][1] - d[0][1] * d[1][0])
            adjuncta.append(d_i_j)
        Adjuncta.append(adjuncta)
    print("Adjuncta este = ", Adjuncta)
    return Adjuncta


Adjuncta = adjuncta(T)


def inversa(Adjuncta):
    det = determinantul(Matrix)
    Inversa = [[j * (1 / det) for j in i] for i in Adjuncta]
    print("Inversa este = ", Inversa)
    return Inversa

Inversa = inversa(Adjuncta)

def matricea_X(B, Inversa):
    result = []
    for i in range(0, 3):
        total = 0
        for j in range(0, 3):
            total += Inversa[i][j] * B[j]
        result.append(total)
    print("X este = ", result)
    return result

matricea_X(B, Inversa)


# CU NUMPY
print(A_np)

# list to np array
A_np = numpy.asarray(A_np)
print(A_np)

# np-array to matrix shape
Matrix_np = A_np.reshape((3, 3))
print("Matricea A = ", Matrix_np)

# determinantul
det_np = numpy.linalg.det(Matrix_np)
print("Determinantul este = ", det_np)

# np-traspusa
T_np = numpy.transpose(Matrix_np)
print("Transpusa = ", T_np)

# np-adjuncta = ?
print("Adjuncta = ", numpy.linalg.inv(Matrix_np) * numpy.linalg.det(Matrix_np))

# np - inversa
Inversa_np = numpy.linalg.inv(Matrix_np)
print("Inversa matricei = ", Inversa_np)

# Matricea X
X_np = numpy.dot(Inversa_np, B)
print("Matricea X este = ", X_np)

#varinata 2
B_np = numpy.asarray(B)
X_np_2 = numpy.linalg.solve(Matrix_np, B)
print("Matricea X cu varinata 2 este = ", X_np_2)






