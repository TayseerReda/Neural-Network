import numpy as np
import pandas as pd 
import random



def preprocess(x):
    #fill null with mean
    for i in x.columns:
        meanval=x[i].mean()
        x[i].fillna(value=meanval, inplace=True)
        #print(x[i])
    return x

def clean(df,class1,class2,feature1,feature2):
    c=0
    for i in df['Class']:
        if(i!=class1 and i!=class2):df=df.drop(c)
        c+=1
     
    for i in df.columns:
        if(i!=feature1 and i!=feature2 and i!='Class'):
            df=df.drop(i,axis=1)             
    return df

def signum(x):
    if(x>0):return 1
    elif(x==0):return 0
    else: return -1



def testing(W,x_test,y_test):
       fail=0
       success=0
       for j in range(len(x_test)):
           xi=np.array(x_test.iloc[j])
           ti=np.array(y_test.iloc[j])
           yi=signum(np.dot(np.transpose(W),xi))
           if(yi!=ti):
               fail+=1
           else:success+=1    
       return fail,success
    
def precptron_train(feature1, feature2, class1, class2, eta, m, bias ):

    
   df=pd.read_excel("Dry_Bean_Dataset.xlsx")
   df=clean(df,class1,class2,feature1,feature2)
   
   x=df.drop(columns='Class')
   
   x=preprocess(x)#fill null with mean
   #print(x.isnull().sum())

   target=[]
   for i in df['Class']:
     if(i==class1):target.append(1)
     elif(i==class2):target.append(-1)
   
   target=pd.DataFrame(target)
   training_x=[]
   training_x=training_x.append(1)#baise
   training_x=x.iloc[:30]
   training_x=training_x.append(x.iloc[50:80])
   
   testing_x=x.iloc[30:50]
   testing_x=testing_x.append(x.iloc[80:])
 
   #print(testing_x.shape)
   
   
   training_y=target.iloc[:30]
   training_y=training_y.append(target.iloc[50:80])
  
   testing_y=target.iloc[30:50]
   testing_y=testing_y.append(target.iloc[80:])
   
   w=[bias,random.randint(1,100)] 
   
   for i in range(m):
       for j in range(len(training_x)):
           xi=np.array(training_x.iloc[j])
           ti=np.array(training_y.iloc[j])
           yi=signum(np.dot(np.transpose(w),xi))
           if(yi!=ti):
               w=w+eta*(ti-yi)*xi
  

   return w,testing_x,testing_y #======>our target


