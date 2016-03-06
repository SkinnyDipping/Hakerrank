# -*- coding: utf-8 -*-
import sys
import numpy as np


def readData(X, y, Q, src="nico"):
    """
    Szczytuje dane z stdin.
    X będzie posiadał listę próbek, w której będzie _m próbek,
    każda próbka to lista składająca się z n cech.
    W y będą wartości wyjściowe dla każdej próbki z X
    (w odpowiadających sobie indeksach).
    Q będzie listą próbek do których należy znaleźć wartość wyjściową.
    Funkcja zwraca 3 wartości:
    m - ilość próbek w zbiorze uczącym,
    n - ilość cech,
    q - ilość próbek w zbiorze szukanym.
    """
    if src != "nico":
        sys.stdin = open(src, "r")
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    n = arr[0]
    m = arr[1]
    for i in range(m):
        t = [float(_t) for _t in input().strip().split(' ')]
        X.append(t[0:n])
        y.append(t[n])
    q = int(input().strip())
    for i in range(q):
        t = [float(_t) for _t in input().strip().split(' ')]
        Q.append(t)
    return n, m, q


def genVars(n, k, p):
    """
    Generuje wariacje z powtórzeniami takie, że
    ze zbioru n elementowego
    k elementowe wariacje
    dla ktorych suma ciągu (będącego elementem wariacji)
    jest mniejsza lub równa p.
    TODO: ta funkcja nie uwzględnia jeszcze n.
    To znaczy, lepiej żeby n > k, bo inaczej siara
    :param n:
    :param k:
    :param p:
    :return:
    """
    var = [0] * k
    var_list = [list(var)]
    while True:
        idx = k - 1
        var[idx] += 1
        while sum(var) > p:
            var[idx] = 0
            idx -= 1
            var[idx] += 1
            if var[0] > p:
                return var_list
        var_list.append(list(var))

def printOutput(tab):
    """
    Printuje tab tak, żeby system hakerranka to łyknął
    :param tab:
    :return:
    """
    for i in tab:
        print(float(i))


def polynomial_regr():
    _X = []
    y = []
    _Q = []
    n, m, q = readData(_X, y, _Q, "input.txt")
    var_list = genVars(0, n, 3)
    var_len = len(var_list)

    # Compute X and Q
    X = []
    Q = []
    for idx in range(m):
        tempX = []
        for i in range(var_len):
            tempx = 1
            for j in range(n):
                tempx *= (_X[idx][j] ** var_list[i][j])
            tempX.append(tempx)
        X.append(tempX)

    for idx in range(q):
        tempQ = []
        for i in range(var_len):
            tempq = 1
            for j in range(n):
                tempq *= (_Q[idx][j] ** var_list[i][j])
            tempQ.append(tempq)
        Q.append(tempQ)

    theta = [0] * var_len

    matX = np.matrix(X)
    maty = np.matrix(y)
    matQ = np.matrix(Q)
    theta = (matX.getT() * matX).getI() * matX.getT() * maty.getT()
    
    output = matQ * theta
    printOutput(output)


polynomial_regr()
