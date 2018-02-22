#List of tuples for Months and date ranges
# + 1 added to avoid confusion of max day range
calendar = [('January', range(1, 31 + 1)),
            ('Feburary', range(1, 28 + 1)),
            ('March', range(1, 31 + 1)),
            ('April', range(1, 30 + 1)),
            ('May', range(1, 31 + 1)),
            ('June', range(1, 30 + 1)),
            ('July', range(1, 31 + 1)),
            ('August', range(1, 31 + 1)),
            ('September', range(1, 30 + 1)),
            ('October', range(1, 31 + 1)),
            ('November', range(1, 30 + 1)),
            ('December', range(1, 31 + 1))]

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def calend(year, start_day,month):
        """
        make_calendar(int, str) --> None
        """
        # Determine current starting position on calendar
        start_pos = week.index(start_day)

        # if True, adjust February date range for leap year | 29 days
        if is_leap(year):
            calendar[1] = ('February', range(1, 29 + 1))

        for month, days in range(1):
            # Print month title
            print('{0} {1}'.format(month, year).center(20, ' '))
            # Print Day headings
            print(''.join(['{0:<3}'.format(w) for w in week]))
            # Add spacing for non-zero starting position
            print('{0:<3}'.format('')*start_pos)
            print "S\tM\tT\tW\tT\tF\tS"
            print (' \t'*start_pos),
            for day in days:

                # Print day

                print day,"\t",
                start_pos += 1
                if start_pos == 7:
                    print""
                    start_pos = 0
            print('\n')
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
month=input("Give me the desired month")
year=int(input('Enter Year'))
strtday = input('Enter start day of the year Mo,Tu,We,Th,Fr,Sa,Su')
calend(year,strtday,month)
