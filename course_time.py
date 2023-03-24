from bs4 import BeautifulSoup
import re
with open("inner.txt") as f:
    soup = BeautifulSoup(f, 'html.parser')

span_tags = soup.find_all('span')
#print(span_tags)

hr_c = re.compile('\dhr.+')
min_c = re.compile('\d+min')

hrs = 0
mins = 0
count = 0
for element in span_tags:
    #print(element.string)
    re_hr = hr_c.match(str(element.string))
    re_min = min_c.match(str(element.string))
    if re_hr:
        print(re_hr)
        e_hr = int(re_hr.group()[0])
        hrs += e_hr
        if len(re_hr.group()) == 8:
            e_min = int (re_hr.group()[4])
            mins += e_min
        else:
            e_min = int(re_hr.group()[4] + re_hr.group()[5])
            mins += e_min
    elif re_min:
        print(re_min)
        if len(re_min.group()) == 4:
            e_min = int (re_min.group()[0])
            mins += e_min
        else:
            e_min = int(re_min.group()[0] + re_min.group()[1])
            mins += e_min
            
total_hrs = hrs + int(mins/60)
rem_mins = str(mins/60)
dec_mins = '0.' + rem_mins.split('.')[1]

print(total_hrs, int(float(dec_mins)*60))
