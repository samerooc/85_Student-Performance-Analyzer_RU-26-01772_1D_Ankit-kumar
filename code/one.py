import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# CSV file read
df = pd.read_csv(
    "students.csv", header=None, names=["name", "maths", "physics", "chemistry"]
)

# EMPTY VARIABLE FOR DIAGRAM SHOW
names = []
maths_marks = []
phy_marks = []
chem_marks = []
totals = []
percentages = []
grades = []

# EVERY STUDENT data check
def check_data():
    for i in range(len(df)):
        row = df.iloc[i]
        name = str(row["name"]).strip()

        # Maths check
        val_m = str(row["maths"]).strip()
        if val_m.isdigit():
            m = float(val_m)
            if m < 0 or m > 100:
                print(f"Invalid marks for {name} in Maths: '{val_m}'. Row skipped.")
                continue
        else:
            print(f"Invalid marks for {name} in Maths: '{val_m}'. Row skipped.")
            continue

        # Physics check
        val_p = str(row["physics"]).strip()
        if val_p.isdigit():
            p = float(val_p)
            if p < 0 or p > 100:
                print(f"Invalid marks for {name} in Physics: '{val_p}'. Row skipped.")
                continue
        else:
            print(f"Invalid marks for {name} in Physics: '{val_p}'. Row skipped.")
            continue

        # Chemistry check
        val_c = str(row["chemistry"]).strip()
        if val_c.isdigit():
            c = float(val_c)
            if c < 0 or c > 100:
                print(f"Invalid marks for {name} in Chemistry: '{val_c}'. Row skipped.")
                continue
        else:
            print(f"Invalid marks for {name} in Chemistry: '{val_c}'. Row skipped.")
            continue

        # Total AND Percentage
        total = m + p + c
        if total.is_integer():
            total = int(total)

        pct = (total / 300) * 100

        # Grade check
        if pct >= 90:
            grade = "A"
        elif pct >= 75:
            grade = "B"
        elif pct >= 60:
            grade = "C"
        elif pct >= 40:
            grade = "D"
        else:
            grade = "F"

        # check test pass OR NO
        names.append(name)
        maths_marks.append(m)
        phy_marks.append(p)
        chem_marks.append(c)
        totals.append(total)
        percentages.append(pct)
        grades.append(grade)


def show_result():
    for i in range(len(names)):
        print(f"{names[i]} | {totals[i]} | {percentages[i]:.2f}% | {grades[i]}")


def show_statistics():
    # find mean, median, std dev
    arr = np.array(percentages)
    mean_pct = np.mean(arr)
    median_pct = np.median(arr)
    std_pct = np.std(arr, ddof=1)

    print(f"Mean %: {mean_pct:.2f} | Median %: {median_pct:.2f} | Std Dev: {std_pct:.2f}")

    # find topper
    max_pct = percentages[0]
    topper_name = names[0]
    for i in range(len(percentages)):
        if percentages[i] > max_pct:
            max_pct = percentages[i]
            topper_name = names[i]

    print(f"Topper: {topper_name} ({max_pct:.2f}%)")

    # Subject average
    m_avg = np.mean(maths_marks)
    p_avg = np.mean(phy_marks)
    c_avg = np.mean(chem_marks)
    print(f"Subject averages: Maths {m_avg:.2f}, Physics {p_avg:.2f}, Chemistry {c_avg:.2f}")

    # Bar Chart
    plt.figure(1)
    plt.bar(names, percentages, color="blue")
    plt.title("Student Percentages")
    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.show()

    # Histogram
    plt.figure(2)
    plt.hist(percentages, bins=5, color="green", edgecolor="black")
    plt.title("Percentage Distribution")
    plt.xlabel("Percentage Range")
    plt.ylabel("Number of Students")
    plt.show()

    print("Bar chart displayed")


# Menu load
def main():
    check_data()
    while True:
        print("\n1. Result")
        print("2. Statistics")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_result()

        elif choice == "2":
            show_statistics()

        elif choice == "3":
            break

        else:
            print("Wrong choice")


main()
