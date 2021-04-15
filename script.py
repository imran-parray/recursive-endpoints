import argparse



parser = argparse.ArgumentParser()
parser.add_argument('--file',help='input file conintaning requests',required=True,type=str)
parser.add_argument('--keepdomain',help='input file conintaning requests',required=False,type=str)
parser.add_argument('--keepparams',help='input file conintaning requests',required=False,type=str)


args = parser.parse_args()

def readfile(file):
	words=[]
	try:
		with open(file,'r') as fh:
			for line in fh:
				words.append(line.rstrip())
				words = [word for word in words if word.strip()]

	except Exception as e:
		pass
	else:
		return words

urls=readfile(args.file)
for urlx in urls:
	if not urlx.strip():
		pass
	url_full=urlx.split('?')
	url=url_full[0];
	params=url_full[1];
	endpointsx=url.split('/')
	endpoints=endpointsx[3:]
	if args.keepdomain=='True':
		end_url=endpointsx[0]+'/'+endpointsx[2]
	else:
		end_url=''
	for endpoint in endpoints:
		end_url=end_url+'/'+endpoint
		if(args.keepparams=='True'):
			print(end_url+'?'+params)
		else:
			print(end_url)