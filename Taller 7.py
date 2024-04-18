# Proyecto que calcula los valores propios y el vector propio usando python y numpy 
import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def calculate_eigen(self):
        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
        return eigenvalues, eigenvectors

# Example usage:
M = Matrix(np.array([[2, 3, 5], [3, 2, 5], [15, 10, 9] ]))
eigenvalues, eigenvectors = M.calculate_eigen()
print(" Valores Propios:")
print(eigenvalues)
print("Vectores Propios:")
print(eigenvectors)

