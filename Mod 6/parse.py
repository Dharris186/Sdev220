from datetime import date
today_string =date(2022, 7, 14)
fmt = "It's %A, %B %d, %Y"
today_string.strftime(fmt)
print (today_string)