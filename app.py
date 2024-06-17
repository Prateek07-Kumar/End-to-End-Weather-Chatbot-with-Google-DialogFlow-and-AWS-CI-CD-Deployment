from flask import Flask
from flask import Flask, request, make_response
import os, json
from flask_cors import CORS,cross_origin
from weather_data import WeatherData