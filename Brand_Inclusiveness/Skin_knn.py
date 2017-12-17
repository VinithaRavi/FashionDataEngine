from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
import numpy as np
import scipy as sp
import imageio
#from sklearn.svm import SVC
#import pickle
from tqdm import tqdm 
from colorthief import ColorThief
import os
import json



#UCI skin dataset
data = sp.genfromtxt("Skin_NonSkin.txt", delimiter = "\t")
results =[]
brands=set()
#sp.random.shuffle(data)
data = np.array(data)
X = data[:, range(0, 3)]
#print(data.shape)
Y = data[:, (len(data[0]) - 1)]
#print(X.shape)
#print(Y.shape)
#KNN classification for Skin and Non skin
def NN_Classify(tr_X, tr_Y, te_X):
	prediction = []
	for te in tqdm(range(0, len(te_X))):	
		distances = (te_X[te, 0] - tr_X[:, 0]) ** 2 + (te_X[te, 1] - tr_X[:, 1]) ** 2 + (te_X[te, 2] - tr_X[:, 2]) ** 2
		nearest = distances.argmin()
		prediction.append(tr_Y[nearest])
	return prediction

def NN_Score(actual, predicted):
	score = 0
	for i in range(0, len(actual)):
		if actual[i] == predicted[i]:
			score += 1
	return score / len(actual)

'''Read all the data''' 
files=[]

for(dirpath, dirnames, filenames) in os.walk("./data"):
	files.extend(filenames)
for file in filenames:
	file_name=os.path.join("./data",file)
	brand=file.split("_")[0]
	brands.add(brand)


	#Read the image to be classified
	#file_name='./skin/Calvin Klein_8b3ead9e-a862-41ec-879b-cb7599d27a87.png'
	img = imageio.imread(file_name)
	#print(img.shape)
	w, h = img.shape[0:2]
	img = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))
	#print(img.shape)

	new_img = np.copy(img)
	new_img[:, [0, 2]] = new_img[:, [2, 0]]
	#print(new_img.shape)

	tr_Y = data[:, (len(data[0]) - 1)]
	tr_X = data[:, range(0, len(data[0]))]
	predicted = np.array(NN_Classify(tr_X, tr_Y, new_img))
	#np.save("predicted.npy",predicted)
	#predicted=np.load("predicted.npy")
	# if skin -white, black otherwise!
	#new_img = np.zeros(shape = (w*h, 3), dtype=np.uint8)



	'''
	Classify the given image on a pixel level as skin and non-skin using knn
	'''

	skin_pixels=0
	skin_cells=np.zeros(shape=(1,3),dtype=np.uint8)
	#print("new image is of : " + str(new_img.shape))
	#print("predicted is of : " + str(predicted.shape))
	#img[:, [2, 0]]=img[:, [0, 2]]
	for i in range(0, len(img)):
		if predicted[i] != 2.0:
			if skin_cells.shape[0]>1:
				skin_cells =np.vstack((skin_cells,img[i]))
			else:
				skin_cells=np.add(skin_cells,img[i] )
			skin_pixels=skin_pixels+1
		else:
			img[i] = [255, 255, 255]
	#print(skin_pixels)

	#np.save("skin_pex_5",skin_cells)
	#print(np.mean(skin_cells,axis=0))
	img = img.reshape((w, h, 3))
	#print(img.shape)
	#print(im.getcolors())
	#print(np.mean(img,axis=0))
	#np.save("image_aftr_trans.npy",img)
	#plt.imshow(img)
	#plt.savefig('test_4_out5.jpg')
	#plt.show()
	#plt.close()
	imageio.imwrite('./output/'+file,img)


	'''find the dominant color in the image'''
	col=ColorThief('./output/'+file)
	dominant_col=col.get_color(quality=1)
	#print(dominant_col)
	color_pallettes=np.asarray([[141,85,36],[198,134,66],[224,172,105],[241,194,125],[255,219,172]])
	#print(color_pallettes)
	#nodes = np.asarray(nodes)

	''' Find the skin tone it matches'''
	dist_2 = np.sum((color_pallettes - dominant_col)**2, axis=1)
	#print(dist_2)
	color_bin=np.argmin(dist_2)+1
	result={"file":file,"color_bin":str(color_bin),"brand":brand,"dominant_color":dominant_col}
	print(result)
	results.append(result)
	
with open('results.json', 'w') as f:
  json.dump(results, f, ensure_ascii=False)







