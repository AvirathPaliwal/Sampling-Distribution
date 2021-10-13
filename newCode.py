import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

print("Mean of the population : ",statistics.mean(data))
print("SD of the population : ",statistics.stdev(data))
print("\n")

fig = ff.create_distplot([data] , ["average"],show_hist=False)
fig.show()

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
    fig = ff.create_distplot([df] , ["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y =[0,12], mode='lines' , name="MEAN"))
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