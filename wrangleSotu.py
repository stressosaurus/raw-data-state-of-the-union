#!/usr/bin/env python3

##!/home/[username]/miniconda3/bin/python

### Converts the main data into table form
## Alex John Quijano
## Created: 3/4/2019

import numpy as np
import sotu as st
import time

# wrangle sotu
start = time.time()
print('--------------------------------------------------')
print('### wrangleSotu.py ###')
print()
print('Downloading State of the Union Speeches...')
print()

# save raw html of sotu links list
sotu_list_url = 'https://www.presidency.ucsb.edu/documents/presidential-documents-archive-guidebook/annual-messages-congress-the-state-the-union'
sotu_table = st.download_sotu(sotu_list_url)
sotu_table.to_pickle('sotu.pkl')
end = time.time()
print('Computing time: '+str(round(end-start,2))+' seconds.')
print()
