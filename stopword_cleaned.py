import time

def stopwd_reduction(inputfile, outputfile):
	start_time = time.time()
	
	infile = open(inputfile, 'r', encoding = 'utf-8')
	outfile = open(outputfile, 'w', encoding = 'utf-8')
	stopword = []
	
	for str in infile.read().split('\n'):
		if str not in stopword:
			stopword.append(str)
			outfile.write(str + '\n')
	
	end_time = time.time()
	print('time for stopwd_reduction is %f'%(end_time - start_time))

if __name__ == '__main__':
	stopwd_reduction('E:/all_stopword.txt', 'E:/stopword.txt')