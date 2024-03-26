import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_iterations():
    x_values = []
    y_values = []

    for n in range(1, 10001):
        iterations = len(collatz_sequence(n)) - 1  # Subtract 1 because the last element is always 1
        x_values.append(iterations)
        y_values.append(n)

    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, marker='o', color='blue', s=5)
    plt.title('Número de Collatz: Número de iteraciones vs Número de inicio')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número de inicio')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_collatz_iterations()
