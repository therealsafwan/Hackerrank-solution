if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input("enter the name")
        score = float(input())
        students.append([name, score])  # Step 1: Store in a nested list

    scores = sorted(set([s[1] for s in students]))  # Unique, sorted scores
    second_lowest = scores[1]  # Step 2: Get second lowest score

    names = [s[0] for s in students if s[1] == second_lowest]  # Step 3: Filter names
    names.sort()  # Step 4: Alphabetical order

    for name in names:
        print(name)
