class GradeEvaluator:

    def __init__(self):

        self.grades = []
        self.avg = 0.0
        self.point_grade = 0.0
        self.letter = ""
        self.remarks = ""

    def collect_grades(self):

        print("GRADE EVALUATION SYSTEM")
        while True:
            try:
                grade_input = input("Enter grade (-1 to stop): ")
                grade = float(grade_input)

                if grade == -1:
                    break
                elif 0 <= grade <= 100:
                    self.grades.append(grade)
                else:
                    print("Invalid input. Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if len(self.grades) == 0:
            print("No valid grades entered.")
            return False

        print("\nEntered Grades:", self.grades)
        return True

    def calculate_metrics(self):

        if not self.grades:
            return

        # Calculate Average
        self.avg = sum(self.grades) / len(self.grades)
        self.avg = round(self.avg, 2)

        # Calculate Point Grade (Formula from original code)
        self.point_grade = ((100 - self.avg) + 10) / 10
        self.point_grade = round(self.point_grade, 2)

    def evaluate_remarks(self):

        if not self.grades:
            return

        # Evaluation Logic (based on original code's specific ranges)
        if self.avg < 50:
            self.remarks = "Dropped"
            self.letter = "F"
        elif self.avg < 75:
            self.remarks = "Failed"
            self.letter = "F"
        elif 75 <= self.avg <= 79:
            self.remarks = "Passed - Satisfactory"
            self.letter = "C"
        elif 80 <= self.avg <= 84:
            self.remarks = "Passed - Good"
            self.letter = "B"
        elif 85 <= self.avg <= 89:
            self.remarks = "Passed - Average"
            self.letter = "B+"
        elif 90 <= self.avg <= 99:
            self.remarks = "Passed - Very Good"
            self.letter = "A"
        elif self.avg == 100:
            self.remarks = "Passed - Excellent"
            self.letter = "A+"

    def display_result(self):

        if self.grades:
            print("\n--- FINAL RESULT ---")
            print("Average Grade:", self.avg)
            print("Point Grade:", self.point_grade)
            print("Letter Grade:", self.letter)
            print("Remarks:", self.remarks)

    def run_evaluation(self):

        if self.collect_grades():
            self.calculate_metrics()
            self.evaluate_remarks()
            self.display_result()

if __name__ == "__main__":
    evaluator = GradeEvaluator()

    evaluator.run_evaluation()
