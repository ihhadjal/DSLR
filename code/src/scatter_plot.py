import describe
import matplotlib.pyplot as plt


def scatter():
   plt.scatter(x=describe.data["Astronomy"], y=describe.data["Defense Against the Dark Arts"])
   plt.title("Correlation between astronomy and defense against the dark arts")
   plt.xlabel("astronomy")
   plt.ylabel("defense against the dark arts")
   plt.show()
def main():
    scatter()

if __name__ == "__main__":
    main()