import numpy as np
import re

def create_datapoint(params):


	w0 = params[1]
	w1 = params[2]
	w2 = params[3]

	line = np.array[w1, w2 ,w0]
	pos_num = params[5]
	neg_num = params[6]

	pos_cnt = 0
	neg_cnt = 0
	pos_point = []
	neg_point = []
	while(pos_cnt < pos_num or neg_cnt < neg_num):
		point = np.random.random(2)
		vec = np.append(point, 1)
		val = np.sign(vec.dot(line))
		
		if val < 0 and neg_cnt < neg_num:
			neg_point.append(point)
			neg_cnt += 1

		elif val > 0 and pos_cnt < pos_num:
			pos_point.append(point)
			pos_num += 1

	pos_point = np.array(pos_point)
	pos_label = np.zeros(pos_num)+1
	pos = np.c_[pos_point, pos_label]

	neg_point = np.array(neg_point)
	neg_label = np.zeros(neg_num)-1
	neg = np.c_[neg_point, neg_label]

	train = np.concatenate((pos, neg), axis=0)

	np.savetxt("train.txt", train, delimiter=",", fmt='%d')







if __name__ == '__main__':
	string = input("DataEmit")
	params = re.split(r'[<,>]\s', string)
	
	create_datapoint(params)



