#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for Weather in January 2015"""

from bs4 import BeautifulSoup
import urllib2

def main():

    print "The following information displays measured and forecasted temp" \
          "eratures for the month of January 2015 in NYC as per the Weath" \
          "er Underground.\n"

    req = urllib2.Request("http://www.wunderground.com/history/airport/KNYC"
                          "/2015/1/1/MonthlyCalendar.html")
    res = urllib2.urlopen(req)
    html_doc = res.read()
    soup = BeautifulSoup(html_doc, 'html5lib')
    list_of_td = soup.find_all('td')

    for entry in list_of_td:
        if "class" in entry.attrs and "day" in entry['class']:
            day_record = entry.find_all('td')
            for entry1 in day_record:
                if "class" in entry1.attrs and "date-link" in entry1['class']:
                    a_table = entry1.find_all('a')
                    for entry10 in a_table:
                        if "class" in entry10.attrs and "dateText" in \
                                entry10['class']:
                            date = int(entry10.string)
                            print "Day of the Month: %i" % date
            data_available = False
            for entry2 in day_record:
                if "class" in entry2.attrs and "value-header" in \
                        entry2['class'] and (entry2.string == "Actual:"\
                                             or entry2.string == "Forecast:"):
                    day_record_temp = entry2.parent
                    type_of_temp = day_record_temp.find("td").string[:-1]
                    temperature_list = day_record_temp.find_all("span")
                    for entry20 in temperature_list:
                        if "class" in entry20.attrs and "high" in \
                                entry20['class']:
                            print "  %s High: %s" % (type_of_temp,
                                                     entry20.string)
                            data_available = True
                        if "class" in entry20.attrs and "low" in \
                           entry20['class']:
                            print "  %s Low: %s" % (type_of_temp,
                                                    entry20.string)
                            data_available = True
            if data_available is False:
                print "  Too far into the future for a forecast"

            print ""


if __name__ == "__main__":
    main()
