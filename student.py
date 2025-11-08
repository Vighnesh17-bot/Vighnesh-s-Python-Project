import csv
import re
import extras
try:
    from extras import student_exam_averages
    flag = True
except ImportError:
    flag = False
def load_exams(filename):
    exams = {}
    current_exam = None

    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or all(cell.strip() == '' for cell in row):
                continue

            if len(row) == 1:
                token = row[0].strip()
                if re.match(r'^(CAT|FAT)\b', token, flags=re.IGNORECASE):
                    current_exam = token.upper()
                    exams.setdefault(current_exam, [])
                    continue
            first = row[0].strip()
            if re.match(r'^(CAT|FAT)\b', first, flags=re.IGNORECASE) and len(row) == 1:
                current_exam = first.upper()
                exams.setdefault(current_exam, [])
                continue

            if current_exam is None:
                continue

            exams[current_exam].append([cell.strip() for cell in row])

    return exams


def stulogin():

    try:
        with open('names.txt', 'r') as nf:
            names = nf.read().split()
            if not names:
                print('')
                return
            student_name = names[0].strip().lower()
    except FileNotFoundError:
        print("names.txt not found.")
        return

    
    try:
        exams = load_exams('subdatabase.csv')
    except FileNotFoundError:
        print("subdatabase.csv not found.")
        return

    if not exams:
        print("No exam data found in subdatabase.csv")
        return

    examlist = list(exams.keys())
    averages=extras.calculate_student_averages()
    logout = 'no'
    while logout.lower() == 'no':
        print('\nChoose between:', ', '.join(examlist))
        print('If you want to see all exam results, type "all exams"\n')

        ex = input('For which exam do you want to see your scores? : ').strip()
        if not ex:
            print("Please enter an exam name.")
            continue

        if ex.upper() in exams:
            print(f'\nResults for {ex.upper()}:\n')
            found = False
            for rec in exams[ex.upper()]:

                if len(rec) >= 3 and rec[0].lower() == student_name:
                    print(f'{rec[1]}: {rec[2]}')
                    found = True
            
            if not found:
                print('No records found for you in this exam.')
        elif ex.lower() == 'all exams':
            print(f'\nAll exam results for {student_name.title()}:\n')
            for exam, data in exams.items():
                print(exam)
                rec_found = False
                for rec in data:
                    if len(rec) >= 3 and rec[0].lower() == student_name:
                        print(f'  {rec[1]}: {rec[2]}')
                        rec_found = True
                #print(averages)
                if not rec_found:
                    print('No records for this student.')
                print()
                
        else:
            print('Invalid exam. Try again.')

        logout = input('Do you want to logout (yes/no)? ').strip().lower()
        if logout not in ('yes', 'no'):

            logout = 'yes' if logout.startswith('y') else 'no'

    print('We wish to see you soon')


if __name__ == '__main__':
    stulogin()
