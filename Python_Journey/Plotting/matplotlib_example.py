import matplotlib.pyplot as plt
import numpy as np

# plot sin(x) over -2pi to 2pi

x = np.linspace(-2*np.pi,2*np.pi,100)
y = np.sin(x)

fig,ax = plt.subplots(1,1) # 1 by 1 grid of axis
lines = ax.plot(x,np.sin(x), "r--", x,np.cos(x),"b--")
fig.suptitle("$sin(x)$ and $cos(x)$ over $-2\\pi$ to $2\\pi$") # this text is called latech text - it uses symbols to say more detailed/mathematical things
plt.show()


# ax.set(xlim=[0,np.pi],ylim=[0,1])
# ax.set(title = "Sin(x)", xlabel="time")
# plt.show() # actually makes plot show up and waits for it to close
