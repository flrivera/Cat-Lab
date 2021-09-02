
def knearest(n=3):

    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split



    # 1. declare the classifier
    # n-neighbors is the number of closest neighbors we consider when voting

    knn=KNeighborsClassifier(n_neighbors=n) # find ideal k

    #2. prepare the unput variable x and target output y

    x,y =Features.drop(['Class'],axis=1),Features['Class'] # we want the input space to only be the features of the flowers

    #3. Split the dataset into two parts, the training set and the test set
    x_test,x_train,y_test,y_train= train_test_split(x,y,test_size=0.3, random_state=1)

    # 4. Fit the model using the training data

    knn.fit(x_train,y_train)

    # 5. make predictions with the input from the test data

    prediction=knn.predict(x_test)



    return(print('kNN(k=3) model, prediction and accuracy:',knn,prediction,knn.score(x_test,y_test)))


def Naives_bayes():
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split

    nb=GaussianNB()

    x,y =Features.drop(['Class'],axis=1),Features['Class']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

    nb.fit(x_train,y_train)

    prediction= nb.predict(x_test)



    return(print('NB model, prediction and accuracy:',nb, prediction,nb.score(x_test,y_test)))


def Des_tree():

    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn import tree

    dtree = DecisionTreeClassifier()
    x,y =Features.drop(['Class'],axis=1),Features['Class']

    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=1)


    dtree.fit(x_train,y_train)

    predictor= dtree.predict(x_test)

    return(print('dtree model, prediction and accuracy:',dtree, predictor,dtree.score(x_test,y_test)))

    
###Train all models and save output
    
