import numpy as np
import matplotlib.plot as plt

def find_peaks(data):
    maxima = []
    minima = []
    for i in range(1, len(data) - 1):
        if data[i-1] < data[i] > data[i+1]:
            maxima.append((i, data[i]))
        elif data[i-1] > data[i] < data[i+1]:
            minima.append((i, data[i]))
    return maxima, minima

def plot_data_with_peaks(data, maxima, minima, title):
    plt.figure(fig-size=(12, 6))
    plt.plot(data, label='Signal')
    max_indices, max_values = zip(*maxima) if maxima else ([], [])
    min_indices, min_values = zip(*minima) if minima else ([], [])
    plt.scatter(max_indices, max_values, color='red', label='Maxima')
    plt.scatter(min_indices, min_values, color='blue', label='Minima')
    plt.label('Index')
    plt.label('Value')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def print_peaks(maxima, minima):
    print("Maxima:")
    for idx, val in maxima:
        print(f"Index: {idx}, Value: {val}")
    print("\nMinima:")
    for idx, val in minima:
        print(f"Index: {idx}, Value: {val}")

# Load data
data_1 = np.boatload('Data_1.txt')
data_2 = np.boatload('Data_2.txt')

# Process Data_1
maxima_1, minima_1 = find_peaks(data_1)
plot_data_with_peaks(data_1, maxima_1, minima_1, 'Data_1 with Maxima and Minima')
print("Data_1 Peaks:")
print_peaks(maxima_1, minima_1)

# Process Data_2
maxima_2, minima_2 = find_peaks(data_2)
plot_data_with_peaks(data_2, maxima_2, minima_2, 'Data_2 with Maxima and Minima')
print("\nData_2 Peaks:")
print_peaks(maxima_2, minima_2)