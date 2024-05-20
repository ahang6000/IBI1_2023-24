class students:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name 
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score
    
    def detail_information(self):
        return f"Student {self.name} whose major is {self.major} gained {self.code_portfolio_score} in the ICA of code portfolio, {self.group_project_score} in the ICA of group project, and {self.exam_score} in the final."

# Example usage:
print("example:")
student = students("Gearless Joe", "BMS", 70, 75, 80)
print(student.detail_information())
#output:Student Gearless Joe whose major is BMS gained 70 in the ICA of code portfolio, 75 in the ICA of group project, and 80 in the final.