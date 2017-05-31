#from PHP to a csv


import urllib2, base64, csv
request = urllib2.Request("http://direct.talentsprint.com:9080/reports/free_user.php")
username = 'report'
password = 'bc1234$'
base64string = base64.b64encode('%s:%s' % (username, password))
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request)
ls = []
with open('skip.csv' , 'w') as f:
    writer = csv.writer(f)
    for line in result:
        writer.writerow([line])

