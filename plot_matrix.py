import matplotlib.image as mpimg
import numpy as np


def generate_random_matrix(m, n):
    return np.random.randint(0, 2, size=(m, n))


def save_matrix(matrix, file_name):
    mpimg.imsave(file_name, matrix)
    return


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
