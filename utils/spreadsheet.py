import pygsheets
import pandas as pd

def insertRow(name, datetime, temperature):
  try:
    #authorization
    gc = pygsheets.authorize(service_file='config/smartHome-afc01dc3da78.json')

    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open('temperature_sensor')

    #select the first sheet
    wks = sh[0]

    wks.append_table(values=[name,datetime,temperature])

    #up`date the first sheet with df, starting at cell B2.
    #wks.set_dataframe(df,(1,1))
  except Exception, e:
    print "Error at spreadsheet writer!"
    print e