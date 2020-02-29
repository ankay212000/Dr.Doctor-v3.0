import matplotlib.pyplot as plt

def visu(inf,filename):
# Pie chart
    labels = ['Infected','Not Infected']
    sizes = [inf,100-inf]
    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = (0, 0.05,)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode,colors=[(1,0,0),(0,1,0)], labels=labels, autopct='%.2f%%',
            shadow=True, startangle=90)# Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal') 
    ax1.set_title("Disease: "+filename) 
    plt.tight_layout()
    plt.show()      