# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
# 读取views.py 里的router
from flask_test.app import views