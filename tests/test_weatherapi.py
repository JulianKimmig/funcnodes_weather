from unittest import IsolatedAsyncioTestCase

from funcnodes_weather.weatherapi import (
    get_weather_data_node,
    hour_forecast_to_dataframe_node,
    plot_wind_node,
    current_weather_series_node,
)
