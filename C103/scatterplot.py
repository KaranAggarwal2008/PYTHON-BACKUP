import pandas as pd
import plotly.express as px

dataFrames = pd.read_csv("data.csv")
framesInGraph = px.scatter(dataFrames, x="Population", y="Per capita",
	          size="Percentage",color="Country",
                   size_max=60)
framesInGraph.show()
