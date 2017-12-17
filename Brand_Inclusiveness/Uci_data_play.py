from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
import numpy as np
import scipy as sp
import imageio
from sklearn.svm import SVC
import pickle

data = sp.genfromtxt("Skin_NonSkin.txt", delimiter = "\t")
# sp.random.shuffle(data)
# data = np.array(data)
# X = data[:, range(0, 3)]
# print(data.shape)
# Y = data[:, (len(data[0]) - 1)]
# print(X.shape)
# print(Y.shape)
# clf = SVC()
# print(clf)
# clf.fit(X, Y) 
filename="svm.sav"
#pickle.dump(clf,open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))




# print("Last 10 rows of Data: \n" + str(data[-10:]))
# print(data.shape)
# Y = data[:, (len(data[0]) - 1)] #equivalent to data[:, 3], we just made it generic
# print("Last 10 labels: \n" + str(Y[-10:]))

# X = data[:, range(0, 3)]
# print("last 10 attributes: \n" + str(X[-10:]))

# def plotter(c, index, plt):
#     label_colors = []
#     for value in Y[:500]:
#     	if value == 1:
#     	    label_colors.append("yellow")
#     	elif index == 0:
#     	    label_colors.append("blue")
#     	elif index == 1:
#     	    label_colors.append("green")
#     	else:
#     	    label_colors.append("red")

#     c.scatter(sp.arange(500), X[:500, index], c = label_colors )
#     if index == 0:
#     	c.set_xlabel("blue")
#     	non_skin_patch = mpatches.Patch(color = "blue", label = "non-skin")
#     elif index == 1:
#     	c.set_xlabel("green")
#     	non_skin_patch = mpatches.Patch(color = "green", label = "non-skin")
#     else:
#     	c.set_xlabel("red")
#     	non_skin_patch = mpatches.Patch(color = "red", label = "non-skin")

#     c.set_ylabel("pixel value")
#     skin_patch = mpatches.Patch(color = "yellow", label = "skin")
#     plt.legend(handles = [skin_patch, non_skin_patch], loc = "upper left")

# fig = plt.figure()
# r = fig.add_subplot(131)
# plotter(r, 0, plt)

# g = fig.add_subplot(132)
# plotter(g, 1, plt)

# b = fig.add_subplot(133)
# plotter(b, 2, plt)
# plt.show(block=True)
# skin_data = data[data[ : , 3] == 1]
# print("min of skin colors: " + str(skin_data[ : , 2].min()))
# print("max of skin colors: " + str(skin_data[ : , 2].max()))
# def slow_Eu_Dist(p1, p2):
#     	return np.sum( (p1-p2)**2)

# def little_faster_Eu_Dist(x, y):
#     	diff = np.array(x) - np.array(y)
#     	return np.dot(diff, diff)

# def faster_Eu_Dist(t, td):
# 	sd = np.zeros(shape = (1, len(td)));
# 	for i in range (0, len(t)):
# 		sd = sd + ((t[i] - td[:, i]) ** 2)
# 	return sd

# from tqdm import tqdm
# def NN_Classify(tr_X, tr_Y, te_X):
# 	prediction = []
# 	for te in tqdm(range(0, len(te_X))):
# 		#distances = np.array([slow_Eu_Dist(tr, te_X[te]) for tr in tr_X])
# 		#distances = np.array([np.linalg.norm(tr - te_X[te]) for tr in tr_X])
# 		#distances = np.array([little_faster_Eu_Dist(tr, te_X[te]) for tr in tr_X])
# 		#distances = faster_Eu_Dist(te_X[te], tr_X)#3":8'
		
# 		# removing a function call overhead makes it ever faster!!		
# 		distances = (te_X[te, 0] - tr_X[:, 0]) ** 2 + (te_X[te, 1] - tr_X[:, 1]) ** 2 + (te_X[te, 2] - tr_X[:, 2]) ** 2
# 		nearest = distances.argmin()
# 		prediction.append(tr_Y[nearest])
# 	return prediction

# def NN_Score(actual, predicted):
# 	score = 0
# 	for i in range(0, len(actual)):
# 		if actual[i] == predicted[i]:
# 			score += 1
# 	return score / len(actual)

# # train_percent = 0.80
# # data_train = data[: int(data.shape[0]*train_percent)]
# # data_test = data[int(train_percent*data.shape[0]) : data.shape[0]]

# # tr_Y = data_train[:, (len(data[0]) - 1)]
# # tr_X = data_train[:, range(0, 3)]
# # te_Y = data_test[:, (len(data[0]) - 1)]
# # te_X = data_test[:, range(0, 3)]

# # predicted = NN_Classify(tr_X, tr_Y, te_X)
# # score = NN_Score(te_Y, predicted)

# # print("Achieved accuracy of " + str(score) + " precents!")
img = imageio.imread('test_4.jpg')
print(img.shape)
w, h = img.shape[0:2]
print(w,h)
img = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))
img[:, [0, 2]] = img[:, [2, 0]]
print(img.shape)
# now we do not mind using all the data
tr_Y = data[:, (len(data[0]) - 1)]
tr_X = data[:, range(0, len(data[0]))]
predicted = loaded_model.predict(img)
print(predicted.shape)

# if skin -white, black otherwise!
new_img = np.zeros(shape = (w*h, 3), dtype=np.uint8)
print("new image is of : " + str(new_img.shape))
print("predicted is of : " + str(predicted.shape))
for i in range(0, len(img)):
    if predicted[i] != 2.0:
        new_img[i] = [255, 255, 255]

new_img = new_img.reshape((w, h, 3))
imageio.imwrite('imageio:astronaut-gray.jpg', new_img[:, :, 0])
import matplotlib.pyplot as plt
plt.imshow(new_img)
plt.savefig('test_4_out1.jpg')
plt.show()
plt.close()
