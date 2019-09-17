FROM python:alpine3.7
copy . /stock_plotter
WORKDIR /stock_plotter
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./stock_plotter.py
