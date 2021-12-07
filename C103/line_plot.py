import pandas as pd

import plotly.express as px

dateFrames = pd.read_csv("line_chart.csv")

framesInGraph = px.line(dateFrames, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

framesInGraph.show()
