<h1>Stock Plotter</h1>

This project utilizes Python and a Flask framework to:
1. Create a page where the user can enter a stock ticker symbol
2. Gather the data for the entered ticker symbol via the Quandl API
3. Plot the data with Bokeh and display it on the next webpage

<h3>Motivation</h3>
This project started as a pre-project to my education with The Data Incubator.  Going forward, it will be a personal work with features added as listed below.

<h3>Contribute</h3>
If you'd like to contribute, the following can be considered as ideas for improvement:
<ul>
  <li><b>Update the API used:</b>  As of April 2018, the Quandl dataset is no longer supported, and therefore does not produce current data.  Obviously, this limits the application of this project, and therefore, this may be the best use of time.</li>
  <li><b>Add a daterange option to the search (/index.html) page</b></li>
  <li><b>Improve the aesthetics of the page</b></li>
  <li><b>Add a dynamic search option with ticker-company name associations listed:</b> In other words, as you type, a dropdown list of companies with names or ticker symbols adhering to the criteria you're typing shoudl populate.</li>
</ul>

<h3>Running the Application</h3>
Download the current version of the GitHub repo, and run the app.py file from the commandline.  This will create a local flask server that you can open up with your web browser to view the contents.
  
<h3>Notes</h3>
Don't forget to take a look at the conda-requirements.txt and requirements.txt file before you start.  Make sure that your system (virtual environment) adheres to these before starting any work.

Also, when editing the code, it's particularly helpful to set 'debug=True' (see the last line of app.py).
