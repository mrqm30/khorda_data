import pandas as pd
import plotly.express as px

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/11_SevCatOneNumNestedOneObsPerGroup.csv"
data = pd.read_csv(url, sep=";")
# Reformat data for the sunburstR package
data = data[data['region'] != ""]
data['path'] = data['region'] + "-" + data['subregion'] + "-" + data['key']
data = data[['path', 'value']]

# Plot
fig = px.sunburst(data, path='path', values='value')
fig.update_layout(legend=dict(traceorder='normal'))
fig.show()
print(data)
