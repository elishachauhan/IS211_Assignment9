#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for NFL Stats"""

from bs4 import BeautifulSoup
import urllib2

def find_column(input_soup, header):
    table = input_soup.find_all('th')
    date_column = None
    header_row = None

    for entry in table:
        if entry.string is not None and \
                        entry.string.lower() == header.lower():
            for i in range(0, len(entry.parent.contents)):
                if entry.parent.contents[i] == entry:
                    date_column = i
    return date_column


def main():
    req = urllib2.Request("http://www.cbssports.com/nfl/stats/playersort/nfl"
                          "/year-2015-season-regular-category-touchdowns/")
    res = urllib2.urlopen(req)
    html_doc = res.read()
    soup = BeautifulSoup(html_doc, 'html5lib')
    table = soup.find_all('a')
    name_column = find_column(soup, "player")
    position_column = find_column(soup, "pos")
    team_column = find_column(soup, "team")
    td_column = find_column(soup, "td")

    print "This script prints out the top 20 players of the NFL by the" \
          " number of touchdowns they have received according\nto the " \
          "cbssports.com website.\n(URL: http://www.cbssports.com/nfl/" \
          "stats/playersort/nfl/year-2015-season-regular-category-touc" \
          "hdowns/)\n"

    counter = 1
    for entry in table:
        if entry['href'][:24] == "/nfl/players/playerpage/":
            player_record = entry.parent.parent
            player_name = player_record.contents[name_column].string
            player_position = player_record.contents[position_column].string
            player_team = player_record.contents[team_column].string
            player_touchdowns = player_record.contents[td_column].string

            print "Name: %s\n Position: %s\n Team: %s\n Touchdowns: %s\n" % \
                  (player_name, player_position, player_team,
                   player_touchdowns)

            counter += 1

        if counter > 20:
            break


if __name__ == "__main__":
    main()
