def read_file(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split(', ') for line in file]

def write_file(filename):
    with open(filename, 'w') as file:
        for name, mark, garde in data:
            file.write["{}, {:.1f}, {}\n".format((name, mark, grade))]

def calculate_weighted_mark(student_data):
    name = student_data[0][0]
    total_mark = sum(float(record[2]) * float(record[3]) / 100) for record in student_data         
        
def determine_grade(weighted_mark):
    if weighted_mark >= 70:
        return "Distinction"      
    elif weighted_mark >= 60:
        return "Merit"
    elif weighted_mark >= 50:
        return "Pass"
    else:
        return "Fail"