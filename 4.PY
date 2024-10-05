#4. Create a histogram to visualize the distribution of values in the array data

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