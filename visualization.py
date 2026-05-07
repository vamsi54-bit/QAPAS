import matplotlib.pyplot as plt

def show_graph(results):
    correct = results.count(1)
    wrong = results.count(0)

    labels = ['Correct', 'Wrong']
    values = [correct, wrong]

    plt.bar(labels, values)

    plt.title("Quiz Performance Analysis")
    plt.xlabel("Result Type")
    plt.ylabel("Number of Questions")

    plt.show()
