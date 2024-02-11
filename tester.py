import matplotlib.pyplot as plt

# Define data
labels = ['Conceive within 1 month', 'Conceive within 2-6 months', 'Conceive within 7-12 months', 'Not conceive within 1 year']
sizes = [0.3, 0.5, 0.2, 0.1]  # Corresponding to the percentages mentioned earlier

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Average Time to Conceive for Healthy Couples Under 35')
plt.show()
