#!/usr/bin/env python
# coding: utf-8

# In[58]:


# Assign a variable for the file to load and the path.
file_to_load = 'Desktop/school/election/Election_Analysis/Resources/election_results.csv'
import os
import csv
# file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = 'Desktop/school/election/Election_Analysis/analysis/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
          
    # Print the header row.
    headers = next(file_reader)
    print(headers)
        
        
        


# In[ ]:







# In[ ]:





# In[ ]:





# In[ ]:




