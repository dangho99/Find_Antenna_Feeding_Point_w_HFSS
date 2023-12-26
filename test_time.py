import os
import time 
import numpy as np 
def get_cpu_load():
	""" Returns percentage of cpu"""
	result = []
	cmd = "WMIC CPU GET LoadPercentage "
	response = os.popen(cmd + ' 2>&1','r').read().strip().split("\r\n")
	#print(response)
	for load in response[1:]:
	   result.append(int(load))

	t = ''
	response = response[0]
	for i in range(18,len(response)):
		t = t + response[i]
	return int(t)

print(get_cpu_load())

 if __name__ == '__main__':
 	temp = []
 	seperate_time = 1/6 
 	start_time = time.time()
 	while True:
 		if (time.time() - start_time) > seperate_time*60:
 			temp.append(get_cpu_load())
 			start_time = time.time()
 			np.savetxt('save.txt',temp,delimiter = ',')
 			print('ok\n')
	
