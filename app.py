from flask import Flask, render_template, request, redirect
import pandas as pd
import quandl
from bokeh.plotting import figure, output_file, save
from bokeh.embed import components

app = Flask(__name__) #create an instance of the flask class (named 'app') in the current file

app.vars={} # Can this be something other than a dictionary? If I only need one ticker at a time, can it be a list, or a string?

# Define interaction on main page
@app.route('/', methods=['GET'])# Ask for a webpage at 127.0.0.1:5000/index and have the stock_plotter accept GET requests
def main():
    return redirect('/index') # With only one view ('/index') is this necessary?

# Define interaction on index page
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# Define interation relative to plot page
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    # Gather the input symbol from the index.html
    app.vars['current_symbol'] = request.form['current_symbol'].upper() # Request the variable 'current_symbol' from the HTML form
    # Set the quandl API key
    quandl.ApiConfig.api_key = 'CD38JS9JqAdmdeio9JPW'
    # Request the data via quandl
    req_data = quandl.get_table('WIKI/PRICES',
                                ticker = app.vars['current_symbol'],
                                qopts = {'columns':['ticker', 'date', 'adj_close']},
                                date = {'gte': '2017-11-01', 'lte': '2017-12-01'},
                                paginate = True)
    req_data.adj_close = round(req_data.adj_close, 2)  # Cleaning data: Reduce to two decimal places
    req_data = req_data.set_index('date')              # Cleaning data: Set the index

    # Configure the plot
    p = figure(x_axis_type='datetime',
               x_axis_label='Date',
               title = app.vars['current_symbol'].upper(),
               y_axis_label = 'Stock Price (USD)',
               plot_width = 800,
               plot_height = 600)
    p.title.text_font_size = '16pt'
    p.title.align = 'center'

    # Plot the data
    p.line(x = req_data.index, y = req_data.adj_close, line_width = 2)
    # Render the bokeh plot on the html page (plot.html)
    script, div = components(p)                                  # Generate JS-digestable components of the plot
    return render_template('plot.html', script=script, div=div)  # script should contain the data for the plot

if __name__ == "__main__":                                       # Ensures that main not assigned when we import other scripts(?)
    app.run(debug=False) #set to false when in production
