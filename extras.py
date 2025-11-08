import csv
import re


def load_exams(filename):
   
    exams = {}
    current_exam = None

    with open(filename, 'r', newline='') as file:
        read = csv.reader(file)
        for rec in read:
            if len(rec) == 1 and rec[0].strip().upper().startswith('CAT'):
                current_exam = rec[0].strip().upper()
                exams[current_exam] = []
            elif current_exam and len(rec) >= 3:
                exams[current_exam].append(rec)
    return exams


def calculate_student_averages():
    student_scores = {}

    try:
        with open('studatabase', 'r') as file:
            current_exam = None
            for line in file:
                line = line.strip()
                if not line:
                    continue

                # Detect exam name (like "CAT 1")
                if ',' not in line:
                    current_exam = line.strip().upper()
                    continue

                # Process student record
                parts = [p.strip() for p in line.split(',')]
                if len(parts) < 3:
                    continue

                student, subject, score = parts[0], parts[1], parts[2]

                try:
                    score = float(score)
                except ValueError:
                    continue

                if student not in student_scores:
                    student_scores[student] = []
                student_scores[student].append(score)

        # Compute average for each student
        averages = {s: sum(sc)/len(sc) for s, sc in student_scores.items() if sc}
        return averages

    except FileNotFoundError:
        print(' File not found.')
        return {}
