import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
# ax.bar([1,2,3,4],[3,2,1,-3])
# ax.plot([0,5],[0,0],"k")

x_locs = np.array([1,2,3,4])  # turning something into a numpy array means you can add and subtract
bar_width = .3
bar_sep = .1

y1_heights = np.array([3,2,1,-3])
y2_heights = np.array([1,2,3,4])

ax.bar(x_locs - bar_width/2 -bar_sep/2,y1_heights,width = bar_width, facecolor = 'r', label ="Red") 
ax.bar(x_locs + bar_width/2 + bar_sep/2,y2_heights,width = bar_width, facecolor = 'k', label = "Black") 
ax.set(xticks = x_locs, xticklabels = ["a","b","c","d"],
       xlabel = "categories",
       ylabel = "values")  
ax.legend() # uses the labels we created previously to make a legend
# ax.barh([1,2], [3,4])
# ax.set(yticks=[1,2],yticklabels=["a very long string", "another super duper long string"])
# plt.tight_layout()
plt.show()

# you're going to have to save the graphs in code - figure it out later