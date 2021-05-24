


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



# line graph
x = np.array([3, 4, 5, 6])
y = x * 3

plt.plot(x, y)
plt.show()

# In[14]:


# bar graph

data = {'english': 20, 'maths': 15, 'history': 30,
        'Python': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(courses, values, color='Red',
        width=0.5)

plt.xlabel("Subjects")
plt.ylabel("No. of students passed")
plt.title("Students passed in different subjects")
plt.show()

# In[17]:


# histogram graph
x = np.random.normal(170, 10, 250)  # 250 value is genrated with standard deviation of 10 and concentrated around 170

plt.hist(x)
plt.show()

# Scatter plot
x = np.array([1,3,2,4,2,5,6,8,9])
y = np.array([99,86,87,88,111,86,86,99,23])

plt.scatter(x, y)
plt.show()


# pie chart

x = np.array([45, 5, 25, 67])
attributes = ["pencil", "pen", "notebook", "sharpner"]

plt.pie(x, labels=attributes, startangle=90)
plt.show()

# In[5]:


# 3d plot

from mpl_toolkits.mplot3d import Axes3D

x = np.random.normal(size=500)
y = np.random.normal(size=500)
z = np.random.normal(size=500)
fig = plt.figure()  # plot figure
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()





