from datetime import timedelta, datetime
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import pandas as pd
from meteoApp.models import Weather
import numpy as np

UNITS = {'temperature': 'C', 'rain': 'mm', 'wind': 'm/s', 'pressure': 'hpa', }


def draw(city, measure, time):
    """
    Prepare basic plot.
    :param city: str city name
    :param measure: str measurement to be plotted (temperature, rain, wind or pressure)
    :param time: str time range for plot (day, week or month)
    """
    data = pd.DataFrame(list(Weather.objects.filter(city=city).values()))
    data.index = pd.to_datetime(data['time'])
    data = data[~data.index.duplicated(keep='first')]
    today = datetime.now()
    time_prior = today - timedelta(days=1)
    if time == 'day':
        time_prior = today - timedelta(days=1)
    elif time == 'week':
        time_prior = today - timedelta(weeks=1)
    elif time == 'month':
        time_prior = today - timedelta(weeks=4)
    data = data[data.index >= time_prior]
    plt.rcParams.update({'font.size': 16})
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.set_xlim([time_prior, datetime.now()])
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
    ax.plot(data[measure], 'bo', markersize=15)
    ax.grid()
    plt.xticks(rotation=30)
    plt.ylabel(measure + ' (' + UNITS[measure] + ')')
    plt.xlabel("time")
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(20)
    ax.yaxis.label.set_fontsize(20)
    ax.tick_params(colors='white')
    fig.savefig('static/images/fig.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()


def draw_wth_trend(city, measure, time):
    """
        Prepare plot with trend line.
        :param city: str city name
        :param measure: str measurement to be plotted (temperature, rain, wind or pressure)
        :param time: str time range for plot (day, week or month)
    """
    data = pd.DataFrame(list(Weather.objects.filter(city=city).values()))
    data.index = pd.to_datetime(data['time'])
    data = data[~data.index.duplicated(keep='first')]
    today = datetime.now()
    time_prior = 0
    if time == 'day':
        time_prior = today - timedelta(days=1)
    elif time == 'week':
        time_prior = today - timedelta(weeks=1)
    elif time == 'month':
        time_prior = today - timedelta(weeks=4)
    data = data[data.index >= time_prior]
    plt.rcParams.update({'font.size': 16})
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.set_xlim([time_prior, datetime.now()])
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
    ax.plot(data[measure], 'bo', markersize=15)

    idx = pd.period_range(time_prior, datetime.now(), freq='H')
    data = data.reindex(idx.to_timestamp(), fill_value=None)
    x = np.arange(len(data.index))
    y = data[measure].values
    z = np.polyfit(x[~np.isnan(y)], y[~np.isnan(y)], 1)
    p = np.poly1d(z)
    trend = pd.DataFrame(p(x), index=data.index)
    ax.plot(trend, "r-", linewidth=3)

    ax.grid()
    plt.xticks(rotation=30)
    plt.ylabel(measure + ' (' + UNITS[measure] + ')')
    plt.xlabel("time")
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_fontsize(20)
    ax.yaxis.label.set_fontsize(20)
    ax.tick_params(colors='white')
    fig.savefig('static/images/fig.png', dpi=300, bbox_inches='tight', transparent=True)
    fig.clf()


def draw_stats(city, measure, time):
    """
        Prepare basic statistics of the data.
        :param city: str city name
        :param measure: str measurement to be plotted (temperature, rain, wind or pressure)
        :param time: str time range for plot (day, week or month)
    """
    data = pd.DataFrame(list(Weather.objects.filter(city=city).values()))
    data.index = pd.to_datetime(data['time'])
    data = data[~data.index.duplicated(keep='first')]
    today = datetime.now()
    time_prior = 0
    if time == 'day':
        time_prior = today - timedelta(days=1)
    elif time == 'week':
        time_prior = today - timedelta(weeks=1)
    elif time == 'month':
        time_prior = today - timedelta(weeks=4)
    data = data[data.index >= time_prior]
    return 'Mean: {}\nStd: {}\nMax: {}\nMin: {}\n'.format(round(data[measure].mean(), 2), round(data[measure].std(), 2),
                                                          round(data[measure].max(), 2), round(data[measure].min(), 2))
