import pandas as pd

import plotly.express as px

#reading data from csv files
dataFrames = pd.read_csv("data.csv")
framesInGraph = px.bar(dataFrames, x='Country', y='InternetUsers')
framesInGraph.show()
