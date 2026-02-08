#Create a "Matrix Operations Tool" using Python and the NumPy library. The application should allow users to input matrices and perform operations like addition, subtraction, multiplication, transpose, and determinant calculation. Include an interactive interface to display results in a structured format.
import numpy as np

def input_matrix(name):
    r = int(input(f"Enter rows of {name}: "))
    c = int(input(f"Enter cols of {name}: "))
    print(f"Enter values row-wise for {name}:")
    mat = []
    for i in range(r):
        row = list(map(float, input().split()))
        mat.append(row)
    return np.array(mat)

while True:
    print("\n--- Matrix Operations Tool ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        print("Result:\n", A + B)

    elif choice == "2":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        print("Result:\n", A - B)

    elif choice == "3":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        print("Result:\n", np.dot(A, B))

    elif choice == "4":
        A = input_matrix("Matrix")
        print("Transpose:\n", A.T)

    elif choice == "5":
        A = input_matrix("Matrix")
        print("Determinant:", np.linalg.det(A))

    elif choice == "6":
        break
1