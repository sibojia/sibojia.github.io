import sys
fout=open('out.txt','w')
for file in sys.argv[1:]:
	lines = list(open(file))
	jp=[];cn=[]
	k=0
	for j in xrange(len(lines)):
		if k==0:
			jp.append(lines[j].strip()+'\\n\\\n');k=1
		else:
			cn.append(lines[j].strip()+'\\n\\\n');k=0
	if k==1: jp.pop()
	fout.write('{\t"title":"",\n\t"jp":"')
	for l in jp:
		fout.write(l)
	fout.write('",\n\t"cn":"')
	for l in cn:
		fout.write(l)
	fout.write('"},\n')