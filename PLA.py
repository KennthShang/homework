import matplotlib.pyplot as plt
import numpy as np

def pla(feature, label):
    w = np.random.uniform(-1,1,size=3)

    flag = 0
    while(flag == 0):
        flag = 1
        for i in range(len(feature)):
            vec = np.append(feature[i], 1)
            y = np.sign(vec.dot(w))

            if label[i] != y:
                w = w + label[i]*vec
                flag = 0
    return w






if __name__ == '__main__':
    file_name = input("PLA ")
    data = np.genfromtxt(file_name, delimiter=',')
    feature = data[:, :-1] 
    label = data[:, -1]
    w = pla(feature, label)

    x = np.arange(0, 1, 0.01)
    y = (w[0] * x1 + w[2]) / (-w[1])
    pos_idx = np.where(label == 1)
    neg_idx = np.where(label == -1)

    pos_data = data[pos_idx]
    neg_data = data[neg_idx]
    plt.scatter(pos_data[:, 0], pos_data[:, 1], color='red')
    plt.scatter(neg_data[:, 0], neg_data[:, 1], color='blue')
    plt.plot(x, y)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

    print("PLA result: <" + str(w[2]) + "," + str(w[0]) + "," + str(w[1]) + ">")