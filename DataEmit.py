import numpy as np
import re

def create_datapoint(params):
    """
    Input: 
        params: <w0, w1, w2> pos_num neg_num
    """
    try:
        # Read in params from input
        w0 = float(params[1])
        w1 = float(params[2])
        w2 = float(params[3])
        pos_num = int(params[5])
        neg_num = int(params[6])
    except:
        print("Input with wrong format")
        return
    else:
        # Initialize the line
        line = np.array([w1, w2 ,w0])
        
    
    
    
    
    # Create dataset
    pos_cnt = 0
    neg_cnt = 0
    pos_point = []
    neg_point = []
    while(pos_cnt < pos_num or neg_cnt < neg_num):
        point = np.round(np.random.random(2)*20-10, 2)
        vec = np.append(point, 1)
        val = np.sign(vec.dot(line))

        if val < 0 and neg_cnt < neg_num:
            neg_point.append(point)
            neg_cnt += 1

        elif val > 0 and pos_cnt < pos_num:
            pos_point.append(point)
            pos_cnt += 1
    
    # Add label to the dataset
    pos_point = np.array(pos_point)
    pos_label = np.zeros(pos_num)+1
    pos = np.c_[pos_point, pos_label]

    neg_point = np.array(neg_point)
    neg_label = np.zeros(neg_num)-1
    neg = np.c_[neg_point, neg_label]
    
    train = np.concatenate((pos, neg), axis=0)
    
    # Save the dataset
    np.savetxt("train.txt", train, delimiter=",", fmt='%.2f')
    print("Create datapoint program finished")






if __name__ == '__main__':
    string = input("DataEmit")
    params = re.split(r'[<,>\s]', string)
    
    create_datapoint(params)
    