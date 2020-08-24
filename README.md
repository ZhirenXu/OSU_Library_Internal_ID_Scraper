# OSU-Library-Internal-ID-Scaper
## What does it do
   Each input url is a webpage of digital collection records, storged as Json. The script will expand that page to 100 records per page (maximum number of displayed records)  
   and extract their internal ids from these records, then using these ids to build url which point to each records. Urls will be outputted in csv file.

## Prerequisites
   Run in Windows10 environment. 
   
   Must have admin level account in OSU library metadata department. 
   
   Python ver. 3.8 or higher, other version has not been tested. 
   
   Required Package: 
   
      MechanicalSoup 
      
      BeautifulSoup 
	  
	  ProgressBar2  
      
   If not installed, please open CMD, go to the path of id scraper folder, then type following command:
   
	  pip install -r dependencies.txt  

   If dependencies.txt doesn't exist or command above has failure, try manually install dependencies by tying following command:
   
      pip install MechanicalSoup 
      
      pip install bs4  
	  
	  pip install progressbar2  
      
## Instruction
1. put csv file which contain DC items' url in the same folder as DC item scrapper. 
2. run 'id scraper.py'  
3. follow instructions on display  
