from flask import Flask, request, render_template, url_for
# from flask.helpers import url_for
from werkzeug.utils import redirect
from getdata import get_data_year,get_data_area

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/pieChart/', methods=['GET','POST'])
def pie():
    year = '2020'
    if request.method == 'POST':
        year = request.form.get('name')
    df_year = get_data_year(year=year)
    return render_template('pieChart.html', Total_North_America=df_year[0],
                           Total_S_Cent_America=df_year[1],Total_Europe=df_year[2],
                           Total_CIS=df_year[3],Total_Middle_East=df_year[4],Total_Africa=df_year[5],
                           Total_Asia_Pacific=df_year[6], Year=year)


@app.route('/stack/', methods=['GET','POST'])
def stack():
    if request.method == 'POST':
        sheetname = request.form.get('name')
        df_area = get_data_area(sheetname)
    else:
        df_area = get_data_area()
    return render_template('stack.html',years=list(df_area.columns), Total_North_America=list(df_area.iloc[0,:]),
                           Total_S_Cent_America=list(df_area.iloc[1,:]),Total_Europe=list(df_area.iloc[2,:]),
                           Total_CIS=list(df_area.iloc[3,:]),Total_Middle_East=list(df_area.iloc[4,:]),Total_Africa=list(df_area.iloc[5,:]),
                           Total_Asia_Pacific=list(df_area.iloc[6,:]))


@app.route('/histogram/', methods=['GET','POST'])
def histogram():
    if request.method == 'POST':
        sheetname = request.form.get('name')
        df_area = get_data_area(sheetname)
    else:
        df_area = get_data_area()
    return render_template('histogram.html',years=list(df_area.columns), Total_North_America=list(df_area.iloc[0,:]),
                           Total_S_Cent_America=list(df_area.iloc[1,:]),Total_Europe=list(df_area.iloc[2,:]),
                           Total_CIS=list(df_area.iloc[3,:]),Total_Middle_East=list(df_area.iloc[4,:]),Total_Africa=list(df_area.iloc[5,:]),
                           Total_Asia_Pacific=list(df_area.iloc[6,:]))

@app.route('/dynamicHistogram/', methods=['GET', 'POST'])
def dynamicHistogram():
    params = request.json if request.method == "POST" else request.args

    # if request.method == "GET":
        
    return  render_template('dynamicHistogram.html')

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)