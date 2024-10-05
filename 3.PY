#3. Display a bar chart to represent the frequency of each item in the given array categories.

# Given data
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]

# Creating a bar chart
plt.bar(categories, values, color='purple')

# Adding labels and title
plt.title('Bar Chart of Categories vs Values')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()
