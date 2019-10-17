## State of the Union Speeches of the United States of America (1790-2019) scraper using beautifulsoup4.
### Alex John Quijano

**Purpose.** The scripts on this repository provides an easy way to scrape the state of the union speeches from https://www.presidency.ucsb.edu/documents/presidential-documents-archive-guidebook/annual-messages-congress-the-state-the-union.

**Instructions.**

1. Clone repository and install the required Python modules.
```bash
git clone https://github.com/stressosaurus/raw-data-state-of-the-union.git
cd raw-data-state-of-the-union/
pip install -r requirements.txt
```

2. Start scraping the website for the speeches by using the command below.
```bash
./wrangleSotu.py
```
The above command will create a 'html_files' folder with the html files of the speeches and a separate 'sotu.npy' will be created containing the processed data for easy access. The data is in a pandas DataFrame format containing columns 'year', 'month', 'day', 'president', 'title', and 'text'.

4. You can open the "sotu.csv" file by using the pandas module in Python.
```python
import pandas as pd
sotu_df = pd.read_csv('sotu.csv',header=0,index_col=0)
print(sotu_df)
```
