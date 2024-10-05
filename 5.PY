#5. Show a pie chart to represent the percentage distribution of different sections in the array `sections`.

# Given data for pie chart
sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]

# Creating a pie chart
plt.pie(sizes, labels=sections, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue', 'lightgreen', 'salmon'])

# Adding a title
plt.title('Pie Chart of Section Distribution')

# Ensuring the pie is drawn as a circle
plt.axis('equal')

# Display the pie chart
plt.show()
