import csv
import pandas as pd 
import plotly.express as px


df = pd.read_csv("mathQuiz.csv")

means = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()

figure = px.scatter(means,x= "student_id", y = "level", size = "attempt", color = "attempt")

figure.show()