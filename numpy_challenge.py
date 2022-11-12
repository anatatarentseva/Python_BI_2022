import numpy as np

def matrix_multiplication(x, y):
    return np.dot(x, y)

def multiplication_check(matrices):
    shape = matrices[0].shape
    for i in range(1, len(matrices)):
        if shape[1] != matrices[i].shape[0]:
            return False
        shape = shape[0], matrices[i].shape[1]
    return True

def multiply_matrices(matrices):
    if multiplication_check(matrices):
        tmp = matrices[0]
        for i in range(1, len(matrices)):
            tmp = matrix_multiplication(tmp, matrices[i])
        return tmp
    return None

def compute_2d_distance(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

def compute_multidimensional_distance(x, y):
    if x.shape != y.shape:
        return None
    tmp = x - y
    return np.sqrt(np.dot(tmp.T, tmp))

def compute_pair_distances(arr):
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(arr.shape[0]):
        for j in range(i, arr.shape[0]):
            result[i][j] = compute_multidimensional_distance(arr[i], arr[j])
            result[j][i] = result[i][j]
    return result



if __name__ == "__main__":
	arr = np.array([i for i in range(1, 101)])
	print(arr)

	arr = np.arange(1, 101)
	print(arr)

	arr = np.linspace(1, 100, 100, dtype = np.uint32)
	print(arr)

	arr = np.array([1] * 100)
	print(arr)

	arr = np.ones(100, dtype = np.uint32)
	print(arr)

	arr = np.zeros(100, dtype = np.uint32)
	print(arr)

	arr = np.random.randint(1, 100, 100, dtype = np.uint32)  
	print(arr)
