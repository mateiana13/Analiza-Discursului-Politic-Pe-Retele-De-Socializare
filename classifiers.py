import politifacts_preprocessing
import politifacts_features
import politifacts_features_matrix
import twitter_features_matrix
import twitter_preprocessing
import numpy
from sklearn import svm
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn import cross_validation 
from sklearn.metrics.pairwise import linear_kernel
from sklearn.ensemble import GradientBoostingClassifier
import grafice
import classifiers_pickle


data = politifacts_preprocessing.makeNewData()
matrixPolitifacts = politifacts_features_matrix.featuresMatrix(data).transpose()
valoareAdevarPolitifacts = politifacts_features.getValoareAdevar(data)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(matrixPolitifacts, valoareAdevarPolitifacts, test_size = 0.01)


#Support Vector Classifier

def trainSVC():
	print("\t\tSVC:")
	svc = svm.SVC()
	svc.fit(X_train, y_train)
	resultsSVC = svc.predict(matrixTwitter)
	print(resultsSVC)
	print("Scor SVC ",svc.score(X_test,y_test))
	return svc

def saveGBC():
	svc = trainSVC()
	classifiers_pickle.savestate(svc,"SVC.pickle")

def loadSVC():
	svc = classifiers_pickle.loadstate("SVC.pickle")
	return svc

#Gradient Boosting Tree Classifier

def trainGBC():
	print("\t\tGradient Boosting Classifier\n")
	gbc = GradientBoostingClassifier(n_estimators = 1000, learning_rate = 1.0,
      random_state = 0,max_features = 9,max_leaf_nodes = 5).fit(X_train,y_train)
	predicted = gbc.predict(X_test)
	print("Scor GBC ",gbc.score(X_test,y_test))
	return gbc

def saveGBC():
	gbc = trainGBC()
	classifiers_pickle.savestate(gbc,"GBC.pickle")


def loadGBC():
	gbc = classifiers_pickle.loadstate("GBC.pickle")
	return gbc




























































