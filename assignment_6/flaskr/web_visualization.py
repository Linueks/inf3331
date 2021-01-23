import io
from flask import Flask, render_template, Response, request
from flaskr.temperature_co2_plotter import plot_temperature, plot_CO2
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas



app = Flask(__name__)


def plot_png(figure):
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/temp.png')
def temp_image():
    min_year = int(request.args.get('minyear', 1816))
    max_year = int(request.args.get('maxyear', 2012))
    month = request.args.get('month', "January")

    return plot_png(plot_temperature('./data/temperature.csv', min_year, max_year, [month])[0])


@app.route('/co2.png')
def co2_image():
    min_year = int(request.args.get('minyear', 1816))
    max_year = int(request.args.get('maxyear', 2012))

    return plot_png(plot_CO2('./data/co2.csv', min_year, max_year))


@app.route('/')
def help_page():


@app.route('/')
def index():
    co2_min_year = int(request.args.get('co2_minyear', 1816))
    co2_max_year = int(request.args.get('co2_maxyear', 2012))
    temp_min_year = int(request.args.get('temp_minyear', 1816))
    temp_max_year = int(request.args.get('temp_maxyear', 2012))
    month = request.args.get('temp_month', "January")

    co2_query_string = f"?minyear={co2_min_year}&maxyear={co2_max_year}"
    temp_query_string = f"?minyear={temp_min_year}&maxyear={temp_max_year}&month={month}"

    return render_template('index.html',
        params=request.args,
        co2_query_string=co2_query_string,
        temp_query_string=temp_query_string)
