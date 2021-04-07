import numpy as np


class my_linalg():
    copy = __import__('copy')
    """Сложение и вычитание"""

    def addition(self, A, B):
        a = len(A)
        b = len(A[0])
        c = len(B)
        d = len(B[0])
        if a != c or b != d:
            return None
        else:
            matrix = [[A[i][j] + B[i][j] for j in range(a)] for i in range(b)]
        return matrix

    def subtraction(self, A, B):
        a = len(A)
        b = len(A[0])
        c = len(B)
        d = len(B[0])
        if a != c or b != d:
            return None
        else:
            matrix = [[A[i][j] - B[i][j] for j in range(a)] for i in range(b)]
        return matrix

    """умножение матрицы"""

    def multyply(self, A, B):
        a = len(A)
        b = len(A[0])
        c = len(B)
        d = len(B[0])
        matrix = [[0 for i in range(d)] for j in range(a)]
        if b == c:
            for i in range(a):
                for j in range(d):
                    matrix[i][j] = sum(A[i][k] * B[k][j] for k in range(c))
            return matrix

    """Находит определитель матрицы"""

    def del_matrix(self, matrix, i, j):
        """убераем столбец и строку в подматрице"""
        new_matrix = self.copy.deepcopy(matrix)
        # self.elem = new_matrix[0][j]
        del new_matrix[i]
        for i in range(len(new_matrix)):
            del new_matrix[i][j]
        return new_matrix

    def det(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        if n != m:
            return None
        if n == 1:
            return matrix[0][0]
        d = 0
        sign = 1  # каждое 2-е значение должно быть с "-"
        for j in range(n):
            d += sign * matrix[0][j] * self.det(self.del_matrix(matrix, 0, j))
            # print(d)
            sign *= -1
        return d

        """Транспонирование"""

    def transponse(self, A):
        a = len(A)
        b = len(A[0])
        matrix = [[A[j][i] for j in range(a)] for i in range(b)]
        return matrix

        """Находит обратную матрицу"""
        """Находит определитель матрицы"""

    def del_mat_inv(self, matrix, i, j):
        """убераем столбец и строку в подматрице"""
        new_matrix = self.copy.deepcopy(matrix)
        self.elem = new_matrix[0][j]
        del new_matrix[i]
        for i in range(len(new_matrix)):
            del new_matrix[i][j]
        return new_matrix

    def inv_pred(self, matrix, det_A):
        sign = 1
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            d = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
            return d
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.inv_matrix[i][j] = sign * self.inv_pred(self.del_mat_inv(matrix, i, j), det_A) / det_A
                sign *= -1
        return self.inv_matrix

    def inv(self, matrix):
        det_A = self.det(matrix)
        n = len(matrix)
        m = len(matrix[0])
        """"Если det == 0 то обратной матрицы не существует"""
        if det_A == 0 and det_A == None:
            return None
        elif n != m:
            return None
        matrix = self.transponse(matrix)
        self.inv_matrix = [[0 for k in range(len(matrix))] for l in range(len(matrix))]
        inv_matrixs = self.inv_pred(matrix, det_A)
        return inv_matrixs


A = [[2, 1, 5],
     [1, 6, 2],
     [3, 5, 8]]
B = [[4, 2, 5],
     [6, 5, 4],
     [9, 8, 9]]
lingalg = my_linalg()

print('определитель', lingalg.det(A))
print('обратная матрица', lingalg.inv(A))
# print(np.linalg.det(A))
print(np.linalg.inv(A))
print("сложение", lingalg.addition(A, B))
print(np.array(A) + np.array(B))
print('вычитание', lingalg.subtraction(A, B))
print('транспонирование', lingalg.transponse(A))
print('умножение', lingalg.multyply(A, B))
print(np.array(A) @ np.array(B))
