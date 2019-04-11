from tkinter import filedialog
from tkinter import *

import csv
import urllib.request, urllib.parse, urllib.error
import os
import requests 
from bs4 import BeautifulSoup 
from page import parsePage
from fields import status_fields,value_fields
class ReadCSVClass:
    """
    GUI Application which counts how many visitors enter the building.
    The application prints the count of visitors in the console
    """
    def __init__(self, master):
        self.master = master

    def subscribe(self, fn):
        self.fn = fn
    def update(self, update):
        if self.fn is not None:
            self.fn(update)
    def readCSV(self, filename):
        with open(filename, 'r') as File:
            csv_reader = csv.reader(File, delimiter=',')
            next(csv_reader)
            
            # return csv_reader
            results = []

            for line in csv_reader:
                self.update("Fetching - Desktop " + line[0])
                pageUrl = line[0]
                urlToOpen = "https://developers.google.com/speed/pagespeed/insights/?url="+pageUrl+"&tab=desktop"
                result = parsePage(urlToOpen)
                result['URLs'] = pageUrl
                result['Device'] = 'desktop'
                results.append(result)
                self.update("Fetching - Mobile " + line[0])
                urlToOpen = "https://developers.google.com/speed/pagespeed/insights/?url="+pageUrl+"&tab=mobile"
                result = parsePage(urlToOpen)
                result['URLs'] = pageUrl
                result['Device'] = 'mobile'
                results.append(result)                
            return results
        #     #print(results)
        # results = [{'Preload key requests': 'Average', 'Properly size images': 'Average', 'Defer unused CSS': 'Average', 'Ensure text remains visible during webfont load': 'Critical', 'Avoid an excessive DOM size': 'Average', 'Serve static assets with an efficient cache policy': 'Average', 'Minimize main-thread work': 'Average', 'Minimize Critical Requests Depth': '14 chains found', 'Eliminate render-blocking resources': 'Good', 'Defer offscreen images': 'Good', 'Minify CSS': 'Good', 'Minify JavaScript': 'Good', 'Efficiently encode images': 'Good', 'Serve images in next-gen formats': 'Good', 'Enable text compression': 'Good', 'Preconnect to required origins': 'Good', 'Server response times are low (TTFB)': 'Good', 'Avoid multiple page redirects': 'Good', 'Use video formats for animated content': 'Good', 'Avoids enormous network payloads': 'Good', 'User Timing marks and measures': 'Good', 'JavaScript execution time': 'Good', 'Minimizes main-thread work': 'Good'}, {'Defer unused CSS': 'Critical', 'Reduce server response times (TTFB)': 'Critical', 'Eliminate render-blocking resources': 'Critical', 'Defer offscreen images': 'Critical', 'Serve images in next-gen formats': 'Average', 'Avoid an excessive DOM size': 'Critical', 'Minimize main-thread work': 'Critical', 'Ensure text remains visible during webfont load': 'Critical', 'Reduce JavaScript execution time': 'Critical', 'Serve static assets with an efficient cache policy': 'Average', 'Minimize Critical Requests Depth': '19 chains found', 'Properly size images': 'Good', 'Minify CSS': 'Good', 'Minify JavaScript': 'Good', 'Efficiently encode images': 'Good', 'Enable text compression': 'Good', 'Preconnect to required origins': 'Good', 'Avoid multiple page redirects': 'Good', 'Preload key requests': 'Good', 'Use video formats for animated content': 'Good', 'Avoids enormous network payloads': 'Good', 'User Timing marks and measures': 'Good', 'Avoid enormous network payloads': 'Average'}]
            # col = status_fields + value_fields
            # try:
            #     with open('page.csv', 'w') as csvfile:
            #         writer = csv.DictWriter(csvfile, fieldnames=col, extrasaction='ignore')
            #         writer.writeheader()
            #         for data in results:
            #             writer.writerow(data)
            # except IOError:
            #     print("I/O error") 

                