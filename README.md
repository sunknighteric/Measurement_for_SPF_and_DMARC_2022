# Measurement Study of SPF and DMARC

##Introduction
We implement two assessments in the scope of the Alexa Top Million ranked domains in September 2021 and March 2022. First we truncated the root domains of all the domains in the list and de-duplicated them, leaving only 224,789 individual domains as the dataset for our tests. The domain list is in /Alexa top one million domain list(De-duplicated version).

All results is got in March 2022, with a detailed list of complete MX, SPF, DMARC and SPF subdomain records for all domains in the list.

dig_crawl.py and dataprocess.py are two scripts we used to get the testing results and help analysis the data. We hope the scripts can help you.

##SPF Trend Statistics

Main Domain:
<img width="336" alt="1679569261271" src="https://user-images.githubusercontent.com/32115816/227183570-cba3a5c0-70bb-4c4f-b762-bcb0585c3621.png">

Subdomain:
<img width="255" alt="1679569313617" src="https://user-images.githubusercontent.com/32115816/227183778-1a16b713-fab9-42f8-8b7b-d31d22606a3e.png">

##DMARC Trend Statistics

Main Domain:
<img width="318" alt="1679569350520" src="https://user-images.githubusercontent.com/32115816/227183918-40ee362d-d46b-4d66-9b1a-7ca95cc7f2df.png">

Subdomain:
<img width="239" alt="1679569376002" src="https://user-images.githubusercontent.com/32115816/227184020-ab5dd1cf-adc6-4e28-b729-8a30ce61b56e.png">
