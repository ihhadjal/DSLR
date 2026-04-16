import describe
import matplotlib.pyplot as plt 

def histogram():
    careOMC = describe.data["Care of Magical Creatures"]

    plt.hist(careOMC, bins=10)
    plt.ylabel("Number of students")
    plt.xlabel("Score")
    plt.title("Score distribution for Care of Magical Creatures")
    plt.show()

def main():
    histogram()

if __name__ == "__main__":
    main()