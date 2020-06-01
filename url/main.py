#!/usr/bin/python3

import re
import urllib.request

warnings_uri = 'https://forecast.weather.gov/product_sites.php?site=CRH&product=ADA'
#warnings_uri = 'http://www.nws.noaa.gov/view/national.php?prod=SMW&sid=AKQ'

with urllib.request.urlopen(warnings_uri) as source:
    warnings_text = source.read()
    document = warnings_text.decode("UTF-8")
    title_pattern = re.compile(r"\<h4\>(.*?)\</h4\>")
    print(title_pattern.search(document).groups())
    #print(document)
