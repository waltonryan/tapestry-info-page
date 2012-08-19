#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Ryan Walton on 2012-08-19.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""
from django.shortcuts import render_to_response
from django.template.loader import get_template

def landing_page(request):
    return render_to_response('landing_page.html', )

