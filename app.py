from flask import Flask, render_template
import pandas as pd
import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, "templates"))

@app.route('/')
def dashboard():
    file_path = os.path.join(base_dir, "data/sales_data.csv")
    df = pd.read_csv(file_path)

    # Pass full raw data to JavaScript for client-side filtering
    raw_data = df.to_dict(orient='records')

    # Static values for initial load
    categories = sorted(df['Category'].unique().tolist())
    products = sorted(df['Product'].unique().tolist())
    months = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']

    return render_template('index.html',
        raw_data=json.dumps(raw_data),
        categories=json.dumps(categories),
        products=json.dumps(products),
        months=json.dumps(months)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)