import csv
import pyping
import json

outfilename='output.csv'
infilename='input.csv'

def writeCSV(dns, ip, maxr, minr, avg):
	with open(outfilename, 'a') as csvfile:
	    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    writer.writerow([dns, ip, maxr, minr, avg])
	    return

def pingserver(ip):
	r=pyping.ping(ip)
	if r.ret_code==0:
		ret={}
		ret['destination']=r.destination
		ret['destip']=r.destination_ip
		ret['maxrtt']=r.max_rtt
		ret['avgrtt']=r.avg_rtt
		ret['minrtt']=r.min_rtt
		return ret
	else:
		return False
if __name__ == '__main__':
	writeCSV('DNS Name', 'IP Address', 'Max RTT', 'Min RTT', 'Average RTT')
	with open(infilename, 'rU') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in csvreader:
			resp= pingserver('.'.join(row))
			writeCSV(resp['destination'], resp['destip'], resp['maxrtt'], resp['minrtt'], resp['avgrtt'])








