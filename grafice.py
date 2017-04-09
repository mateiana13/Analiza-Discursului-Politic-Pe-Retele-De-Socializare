import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plotResults(countedResHC,countedResSS,countedResDT):

    # definim setul de culori pt fiecare grafic
    colorsHC=['lightpink','violet']
    colorsSS=['cyan','blue']
    colorsDT=['chartreuse','salmon']
    
    labels='True','False'
    explode = (0,0.1) 
    fig=plt.figure('RESULTS',facecolor='white')


    plt.subplot(221)
    plt.axis('equal')
    plt.title('Results Hillary Clinton')
    plt.pie(countedResHC,explode=explode,labels=labels,colors=colorsHC,autopct='%1.1f%%',shadow=True,startangle=90)
    

    plt.subplot(222)
    plt.axis('equal')
    plt.title('Results Sen Senders')
    plt.pie(countedResSS,explode=explode,labels=labels,colors=colorsSS,autopct='%1.1f%%',shadow=True,startangle=90) 

    plt.subplot(212)
    plt.axis('equal')
    plt.title('Results Donald Trump')
    plt.pie(countedResDT,explode=explode,labels=labels,colors=colorsDT,autopct='%1.1f%%',shadow=True,startangle=90) 
    
    plt.show()



