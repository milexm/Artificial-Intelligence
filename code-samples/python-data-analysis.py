import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def try_numpy():
    # Create a simple array
    a = np.array([1, 2, 3])
    print("Array a:", a)
    # Calculate and print the mean
    print("Mean of a:", np.mean(a))


def try_pandas():

    # Create a simple DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

def try_matplotlib():

    # Plot a simple line chart
    x = [1, 2, 3]
    y = [2, 4, 6]
    plt.plot(x, y, marker='o')
    plt.title("Simple Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()


if __name__ == "__main__":
    try_numpy()
    try_pandas()
    try_matplotlib()