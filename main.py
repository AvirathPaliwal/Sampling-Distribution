import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

print("Mean of the population : ",statistics.mean(data))
print("SD of the population : ",statistics.stdev(data))
print("\n")

fig = ff.create_distplot([data] , ["temperature"],show_hist=False)
#fig.show()

#print("Mean of the Sample : ",statistics.mean(data_set))
#print("SD of the Sample : ",statistics.stdev(data_set))

def randomSetOfMean(counter):
    data_set = []
    for i in range(0,counter):
        rand_index = random.randint(0,len(data) - 1 )
        value = data[rand_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("Mean of Sampling Distribution : " , mean)    
    fig = ff.create_distplot([df] , ["temperature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y =[0,1], mode='lines' , name="MEAN"))
    fig.show()

def setup():
    mlist = []
    for i in range(0,1000):
        setOfMean = randomSetOfMean(100)
        mlist.append(setOfMean)
    show_fig(mlist)

setup()

def std():
    stdlist=[]

    for i in range(0,1000):
        setofmean = randomSetOfMean(100)
        stdlist.append(setofmean)
    sd = statistics.stdev(stdlist)
    print("SD of sampling Distribution is  :  "  , sd)


std()

    
#SD of the sampling mean =  SD Population / sqrt (number of data in each sample)      
#sd of sampling mean = 5.699 / sqrt(100)
## sd of sampling mean = 5.699 / 10