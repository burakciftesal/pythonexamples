import pandas as pd
import matplotlib.pyplot as plt
import csv
from pathlib import Path
from statsmodels.graphics.tsaplots import plot_acf


HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

roster = pd.read_csv(
    DATA_FOLDER / "roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

hw_exam_grades = pd.read_csv(
    DATA_FOLDER / "hw_exam_grades.csv",
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID",
)

quiz_grades = pd.DataFrame()
for file_path in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = " ".join(file_path.stem.title().split("_")[:2])
    quiz = pd.read_csv(
        file_path,
        converters={"Email": str.lower},
        index_col=["Email"],
        usecols=["Email", "Grade"],
    ).rename(columns={"Grade": quiz_name})
    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)
print(quiz_grades)

q1 = pd.DataFrame(quiz_grades, columns=['Quiz 1'])
print(q1)

final_data_exams = pd.merge(
    roster, hw_exam_grades, left_index=True, right_index=True,
)

final_data_quiz = pd.merge(
    final_data_exams, quiz_grades, left_on="Email Address", right_index=True
)

print(final_data_exams)
print(final_data_quiz)
final_data_1 = final_data_exams.fillna(0)
final_data_2 = final_data_quiz.fillna(0)
final_data = (final_data_2 + final_data_1)
print(final_data)