def computeGrades():
    courseCount = int(input("Enter How many courses do you have: "))
    coursesItterator = 0;
    totalUnits = 0
    computedAve = 0
    while coursesItterator !=  courseCount:
        course = input("Enter Course Code: ")
        units = int(input("Enter number of units: "))
        grade = float(input("Enter your grades: "))
        totalUnits += units
        computed = grade * units
        computedAve += computed
        computedGWA = computedAve / totalUnits
        coursesItterator += 1

    if coursesItterator ==  courseCount:
        print(f'GWA: {computedGWA:.2f}')
    input("Enter any key to exit!")
computeGrades()