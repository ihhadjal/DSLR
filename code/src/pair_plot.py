import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import describe


def pair_plot():
    courses = describe.COURSES
    data = describe.data

    sns.pairplot(data, vars=courses, hue="Hogwarts House")
    
    plt.tight_layout()

    plt.savefig('pair_plot.png', dpi=300) 

    plt.close()
def main():
    pair_plot()

if __name__ == "__main__":
    main()