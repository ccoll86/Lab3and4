#retrieving log fles across network and creating new local location for the data
from urllib.request import urlretrieve
URL_PATH="https://s3.amazonaws.com/tcmg476/http_access_log"
Local_Copy='aws.log'
headers=urlretrieve(URL_PATH, Local_Copy)


#reading file to look for 2 patterns
total_log_requests=0
past_year_requests=0

file = open("aws.log", "r")

#start looking for total log requests
lines = file.readlines()
for line in lines:
    if(len(line)>=56):
        total_log_requests+=1
return(total_log_requests)

#start looking for log requests made in the last year
lines = file.readlines()
import datetime
import re
now = datetime.datetime.now
earlier = datetime.datetime(2019, 9, 17)

for line in lines:
    data = lines.split()
    date = data[3][1::].split(':')
    if re.search(earlier>date<=now, line):
          past_year_requests+=1
return(past_year_requests)

#print the output results
print('The requests made total: ', total_log_requests) 
print('The requests made last year: ', past_year_requests)



