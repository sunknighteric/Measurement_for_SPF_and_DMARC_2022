# email_assessment_2022

This project is for paper "SPF and DMARC-based Mitigation and Assessment Methodology for Secure Email Systems".

We implement two assessments in the scope of the Alexa Top One Million ranked domains in September 2021 and March 2022. First we truncated the root domains of all the domains in the list and de-duplicated them, leaving only 224,789 individual domains as the dataset for our tests. The domain list is in /Alexa top one million domain list(De-duplicated version).

All results is got in March 2022, with a detailed list of complete MX, SPF, DMARC and SPF subdomain records for all domains in the list.

dig_crawl.py and data_processing.py are two scripts we used to get the testing results and help analysis the data. We hope the scripts can help you.
