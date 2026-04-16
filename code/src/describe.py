import pandas as pd
import math
import sys

data_sets = sys.argv[1]
indexes = ["Count", "Mean", "STD", "Min", "25%", "50%", "75%", "Max"]
COURSES = [
    "Arithmancy",
    "Astronomy",
    "Herbology",
    "Defense Against the Dark Arts",
    "Divination",
    "Muggle Studies",
    "Ancient Runes",
    "History of Magic",
    "Transfiguration",
    "Potions",
    "Care of Magical Creatures",
    "Charms",
    "Flying",
]

try:
    data = pd.read_csv(data_sets)
except(ValueError, pd.errors.EmptyDataError):
    print("error: could not read the data")

def Count(feature):
    count = 0
    for i in feature:
        if not pd.isna(i):
            count += 1
    return count

def Mean(feature):
    count = Count(feature)
    if (count < 2):
        return ("nan")
    Sum = 0
    for i in feature:
        Sum += i
    mean = Sum / count
    return mean

def Std(feature):
    count = Count(feature)
    if count < 2:
        return ("nan")
    mean = Mean(feature)
    Sum = 0
    for i in feature:
        d = i - mean
        Sum += d * d
    return math.sqrt(Sum / (count - 1))

def Min(feature):
    m = feature[0]
    for i in feature[1:]:
        if i < m:
            m = i
    return m

def Max(feature):
    m = feature[0]
    for i in feature[1:]:
        if i > m:
            m = i
    return m

def percentile(feature, percent):
    count = Count(feature)
    pos = (count - 1) * percent
    low = int(math.floor(pos))
    high = int(math.ceil(pos))

    if low == high:
        return feature[low]
    weight = pos - low
    return feature[low] * (1.0 - weight) + feature[high] * weight

def describe(feature):
    values = []
    for i in feature:
        if not pd.isna(i):
            values.append(i)
    values.sort()

    return [
        Count(values),
        Mean(values),
        Std(values),
        Min(values),
        percentile(values, 0.25),
        percentile(values, 0.50),
        percentile(values, 0.75),
        Max(values),
    ]

def build_data_frame():
    df = pd.DataFrame(index=indexes)

    for course in COURSES:
        df[course] = describe(data[course])

    return df

def main():

    df = build_data_frame()

    print(df)

if __name__ == "__main__":
    main()