import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the student data from the CSV file
try:
  df = pd.read_csv(
      "students.csv", header=None, names=["name", "maths", "physics", "chemistry"]
  )
except FileNotFoundError:
  print(
      "Couldn't find 'students.csv'. Please make sure the file is in the same"
      " folder."
  )
  exit()
except Exception as e:
  print(f"Something went wrong while reading the file: {e}")
  exit()

# Lists to store clean, verified student records for charts and results
names = []
maths_marks = []
phy_marks = []
chem_marks = []
totals = []
percentages = []
grades = []


# Go through each student's row and validate their marks
def check_data():
  for i in range(len(df)):
    row = df.iloc[i]
    name = str(row["name"]).strip()

    # Check Maths score
    val_m = str(row["maths"]).strip()
    try:
      m = float(val_m)
      if m < 0 or m > 100:
        print(
            f"Skipping {name} — Maths marks ({val_m}) must be between 0 and"
            " 100."
        )
        continue
    except ValueError:
      print(f"Skipping {name} — '{val_m}' is not a valid number for Maths.")
      continue

    # Check Physics score
    val_p = str(row["physics"]).strip()
    try:
      p = float(val_p)
      if p < 0 or p > 100:
        print(
            f"Skipping {name} — Physics marks ({val_p}) must be between 0 and"
            " 100."
        )
        continue
    except ValueError:
      print(f"Skipping {name} — '{val_p}' is not a valid number for Physics.")
      continue

    # Check Chemistry score
    val_c = str(row["chemistry"]).strip()
    try:
      c = float(val_c)
      if c < 0 or c > 100:
        print(
            f"Skipping {name} — Chemistry marks ({val_c}) must be between 0 and"
            " 100."
        )
        continue
    except ValueError:
      print(
          f"Skipping {name} — '{val_c}' is not a valid number for Chemistry."
      )
      continue

    # Calculate total and overall percentage
    total = m + p + c
    if total.is_integer():
      total = int(total)

    pct = (total / 300) * 100

    # Assign grade based on percentage
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

    # Save valid student details into our lists
    names.append(name)
    maths_marks.append(m)
    phy_marks.append(p)
    chem_marks.append(c)
    totals.append(total)
    percentages.append(pct)
    grades.append(grade)


# Print the final scorecard for all valid students
def show_result():
  if len(names) == 0:
    print("No valid student records found to display.")
    return

  print("\n--- Student Results ---")
  for i in range(len(names)):
    print(
        f"{names[i]} | Total: {totals[i]} | {percentages[i]:.2f}% | Grade:"
        f" {grades[i]}"
    )


# Calculate class stats and plot the graphs
def show_statistics():
  try:
    # Basic class statistics
    arr = np.array(percentages)
    mean_pct = np.mean(arr)
    median_pct = np.median(arr)
    std_pct = np.std(arr, ddof=1)

    print("\n--- Class Performance ---")
    print(
        f"Average: {mean_pct:.2f}% | Median: {median_pct:.2f}% | Std Dev:"
        f" {std_pct:.2f}"
    )

    # Find who scored the highest
    max_pct = percentages[0]
    topper_name = names[0]
    for i in range(len(percentages)):
      if percentages[i] > max_pct:
        max_pct = percentages[i]
        topper_name = names[i]

    print(f"Class Topper: {topper_name} ({max_pct:.2f}%)")

    # Average marks per subject
    m_avg = np.mean(maths_marks)
    p_avg = np.mean(phy_marks)
    c_avg = np.mean(chem_marks)
    print(
        f"Subject Averages -> Maths: {m_avg:.2f} | Physics: {p_avg:.2f} |"
        f" Chemistry: {c_avg:.2f}"
    )

    # Plot 1: Individual student percentages
    plt.figure(1)
    plt.bar(names, percentages, color="blue")
    plt.title("Student Percentages")
    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.show()

    # Plot 2: Score distribution across the class
    plt.figure(2)
    plt.hist(percentages, bins=5, color="green", edgecolor="black")
    plt.title("Percentage Distribution")
    plt.xlabel("Percentage Range")
    plt.ylabel("Number of Students")
    plt.show()

    print("Charts closed successfully.")

  except IndexError:
    print("Not enough valid student data to generate statistics.")
  except Exception as e:
    print(f"Ran into an issue while generating stats or charts: {e}")


# Main menu loop to interact with the user
def main():
  check_data()

  while True:
    try:
      print("\n1. View Results")
      print("2. View Statistics & Charts")
      print("3. Exit")
      choice = input("Pick an option (1-3): ").strip()

      if choice == "1":
        show_result()

      elif choice == "2":
        show_statistics()

      elif choice == "3":
        print("Exiting program. Goodbye!")
        break

      else:
        print("Invalid option. Please enter 1, 2, or 3.")

    except Exception as e:
      print(f"Unexpected error: {e}")


main()
