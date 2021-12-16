import csv
import pandas as pd

import plotly.graph_objects as go

df = pd.read_csv("mathQuiz.csv")

studentDF = df.loc[df["student_id"]=="TRL_987"]

means = studentDF.groupby("level")["attempt"].mean()

figure = go.Figure(go.Bar(
    x = means,
    y = ["Level 1", "Level 2","Level 3", "Level 4"],
    orientation = "h"
))

figure.show()

