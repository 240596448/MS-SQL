import requests

data_urls = (
		{
			"Version" : "2005",
			"FileName" : "SQL Server 2005 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/pcvyzrhymde23c2/SQL%20Server%202005%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2008",
			"FileName" : "SQL Server 2008 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/5xhzwxad3k05pah/SQL%20Server%202008%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2008R2",
			"FileName" : "SQL Server 2008 R2 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/a7i1nbzaqn89jav/SQL%20Server%202008%20R2%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2012",
			"FileName" : "SQL Server 2012 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/ahlz1dkrvg2gd2n/SQL%20Server%202012%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2014",
			"FileName" : "SQL Server 2014 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/wdypigf3lvbmy3h/SQL%20Server%202014%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2016",
			"FileName" : "SQL Server 2016 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/r63yxa1lptce1qm/SQL%20Server%202016%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2016SP2",
			"FileName" : "SQL Server 2016 SP2 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/phr212rsjdcasl2/SQL%20Server%202016%20SP2%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2017",
			"FileName" : "SQL Server 2017 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/wmsfaqks7lwzqe4/SQL%20Server%202017%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
		{
			"Version" : "2019",
			"FileName" : "SQL Server 2019 Diagnostic Information Queries.sql",
			"URL" : "https://www.dropbox.com/s/p1urkrq5v01cuw3/SQL%20Server%202019%20Diagnostic%20Information%20Queries.sql?dl=1",
		},
	)


print('Downloading...')

for i in data_urls:

	rsps = requests.get(i['URL'])

	if rsps.status_code == 200:
		file = open(i['FileName'], 'bw')
		file.write(rsps.content)
		file.close()
		print('Version {}: OK'.format(i['Version']))

	else:
		print('Version {}: get response {}'.format(i['Version'], rsps.status_code))

print('Complette')
