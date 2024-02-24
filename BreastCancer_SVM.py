from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def MarvellousSVM():
    #Load dataset
    cancer = datasets.load_breast_cancer()

    #print the label type of cancer('malignant' 'benign')
    print("Labels of the cancer dataset :", cancer.target_names)

    #print data(feature) shape
    print("Shape of dataset is :",cancer.data.shape)

    #print the cancer data features (top 5 records)
    print("First 5 records are :")
    print(cancer.data[0:5])

    #print the cancer labels (0:malignant, 1:benign)
    print("Target of dataset : ",cancer.target)

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109) # 70% training and 30% test

    #create a svm classifier
    clf = svm.SVC(kernel='linear')#Linear Kernel

    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #predict the response for test dataset
    y_pred = clf.predict(X_test)

    #Model Accuracy : how often is the classifier correct?
    print("Accuracy of the model is :",metrics.accuracy_score(y_test, y_pred)*100)


def main():
    print("____Marvellous Support Vector Machine____")

    MarvellousSVM()

if __name__=="__main__":
    main()


