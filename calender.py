import calendar
# To ask month and year from the user
yy = int(input("Enter year: "))
calendar.prcal(yy)
#display the year calendar 
print ('')
mm = int(input("Enter month: "))

# display the month calendar
print(calendar.month(yy, mm))
