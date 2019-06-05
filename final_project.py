# Kexin Wei, Section AC, uwnetid: wkx98
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cse163_utils  # noqa: F401


def relate_to_class_size(data):
    sns.lmplot(x="Student_Count", y="Average_GPA",
               truncate=True, height=5, data=data)


def main():
    sns.set()
    data = pd.read_csv('1143333_PR00015CSV_2019-01-23.csv')
    relate_to_class_size(data)


if __name__ == '__main__':
    main()
