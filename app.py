from codecarbon.viz.carbonboard import render_app
import pandas as pd

df = pd.read_csv("emissions.csv")

app = render_app(df)

server = app.server

if __name__ == "__main__":
    app.run_server(port=8080,host='0.0.0.0',debug=True)
