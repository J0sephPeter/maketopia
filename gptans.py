# Input string
data = "Alice:82,Bob:91,carol:74,dan:91,ellen:59"

# Parse and normalize
students = []
for entry in data.split(','):
    try:
        name, grade = entry.split(':')
        name = name.strip().title()       # Normalize name
        grade = int(grade.strip())        # Convert grade to integer
        students.append((name, grade))
    except ValueError:
        # Skip invalid entries
        continue

# Compute stats
num_students = len(students)
average = round(sum(grade for _, grade in students) / num_students, 2)

max_grade = max(grade for _, grade in students)
top_students = sorted(name for name, grade in students if grade == max_grade)

failing_students = sorted(name for name, grade in students if grade < 60)
passing_students = sorted(
    [(name, grade) for name, grade in students if grade >= 60],
    key=lambda x: x[1],
    reverse=True
)

# Print results
print(f"Valid students: {num_students}")
print(f"Average: {average}")
print(f"Top score: {max_grade} -> {top_students}")
print(f"Failing: {failing_students}")

# Save passing students to file
try:
    with open("passing.txt", "w") as f:
        for name, grade in passing_students:
            f.write(f"{name}:{grade}\n")
    print(f"Saved {len(passing_students)} passing students to passing.txt")
except IOError as e:
    print(f"Error saving passing students: {e}")
