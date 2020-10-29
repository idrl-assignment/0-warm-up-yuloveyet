# TODO: import ...
import numpy as np

def generate_random_matrix(m, n):
    return np.rand(m, n)

def save_matrix(matrix, file_name):
    raise NotImplementedError  # TODO: 删除该行，实现该函数功能


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
