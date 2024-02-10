# Measurement Study of SPF and DMARC

## Introduction

This work is part of our paper **"Subdomain Protection is Needed: An SPF and DMARC-based Empirical Measurement Study and Proactive Solution of Email Security"**. This paper has been accepted by **the 42nd International Symposium on Reliable Distributed Systems (SRDS 2023)**.

Welcome to cite our work.

@INPROCEEDINGS{10419249,

  author={Zhang, Han and Mi, Dengke and Chen, Libo and Liu, Ming and Shi, Yong and Xue, Zhi},
  
  booktitle={2023 42nd International Symposium on Reliable Distributed Systems (SRDS)}, 
  
  title={Subdomain Protection is Needed: An SPF and DMARC-Based Empirical Measurement Study and Proactive Solution of Email Security}, 
  
  year={2023},
  
  pages={140-150},
  
  doi={10.1109/SRDS60354.2023.00023}
  
  }

We implement two assessments in the scope of the Alexa Top Million ranked domains in September 2021 and March 2022. First we truncated the root domains of all the domains in the list and de-duplicated them, leaving only 224,789 individual domains as the dataset for our tests. The domain list is in /Alexa top one million domain list(De-duplicated version).

All results are got in March 2022, with a detailed list of complete MX, SPF, DMARC and SPF subdomain records for all domains in the list.

dig_crawl.py and dataprocess.py are two scripts we used to get the testing results and help analysis the data. We hope the scripts can help you.

## SPF Trend Statistics

Main Domain:

<img width="336" alt="1679569261271" src="https://user-images.githubusercontent.com/32115816/227183570-cba3a5c0-70bb-4c4f-b762-bcb0585c3621.png">

Subdomain:

<img width="255" alt="1679569313617" src="https://user-images.githubusercontent.com/32115816/227183778-1a16b713-fab9-42f8-8b7b-d31d22606a3e.png">

## DMARC Trend Statistics

Main Domain:

<img width="318" alt="1679569350520" src="https://user-images.githubusercontent.com/32115816/227183918-40ee362d-d46b-4d66-9b1a-7ca95cc7f2df.png">

Subdomain:

<img width="239" alt="1679569376002" src="https://user-images.githubusercontent.com/32115816/227184020-ab5dd1cf-adc6-4e28-b729-8a30ce61b56e.png">

## Discussion
In all tested domains, nearly half of the domains have SPF configuration issues and more than **70%** of domains have DMARC configuration problems. Although the adoption rate of SPF and DMARC is slowly growing, there is still a lot of room for improvement. Not surprisingly, more than **90%** of the domains do not implement SPF or DMARC configuration for subdomains. This shows that the protection of subdomains has not yet been taken seriously. Although several previous research efforts have highlighted the problem, SPF and DMARC are still not widely accepted and used by the community, and new email security threats continue to emerge. We hope that this measurement study will serve as a wake-up call to all domain operators and that we will see a significant increase in valid SPF and DMARC usage in the near future.

## Additional Experiments

### Attacks based on SPF and DMARC configuration issues

We simulate four phishing email attack scenarios to explain why wrong configurations can bring phishing attack risks. The domain name of the attacked party is email-target.com. As the attacker, we will fake this domain name to send phishing emails to others. To demonstrate the attack, we use victim@hotmail.com as the recipient of the spoofing mail. We use an open-source SMTP test tool Swaks to send the testing phishing emails.

We select three configuration issues for SPF and one for DMARC, including No SPF Record Found, Too Many Included Lookups, Subdomain No SPF Record for experiment and DMARC using none policy. For Multiple SPF Records and SPF Syntax Error, the experiment results are the same.

#### No SPF Record Found

There is no SPF or DMARC configuration in email-target.com. We send a testing mail in the identity of email-target.com to victim@hotmail.com. The result is shown in Figure (a). So, if a domain has no SPF configuration, any attacker can use simple mail simulation tools to send emails to anyone using the domain. 

<img width="300" alt="1688022834375" src="https://github.com/sunknighteric/Measurement_for_SPF_and_DMARC_2022/assets/32115816/5ec37e9d-b009-4f0c-9f15-867d3107f886">

#### Too Many Included Lookups 

To demonstrate this configuration issue, we add the following two DNS records. We include spf.email-target.com for SPF in main domain, and included email-target.com for SPF in spf.email-target.com. This caused a SPF recursive loop issue, a specific example of Issue. When server requests SPF record of email-target.com, it will request SPF record of spf.email-target.com, and then it will go back to email-target.com and loop. Soon, it will exceed the limit of ten queries and return perm error.

<img width="300" alt="1688022872604" src="https://github.com/sunknighteric/Measurement_for_SPF_and_DMARC_2022/assets/32115816/c2535bf1-d96c-46a9-a6ec-bc4da0e4a9c4">

```
    Type:txt
    Host:email-target.com

    Value:v=spf1 include:spf.email-target.com -all

    Type:txt
    Host:spf.email-target.com

    Value:v=spf1 include:email-target.com -all
```

So, when we use the same method to send phishing email, SPF returns perm error, and the mail is accepted by the receiving server as shown in Figure (b).

#### Subdomain No SPF Record

For the following experiments, we add a TXT record in DNS as follows to initiate SPF and forbid any IP to send mail on behalf of the domain email-target.com.

```
    Type:txt
    Host:email-target.com
    Value:v=spf1 -all
```

In this case, we cannot use the domain email-target.com to send spoof mails. However, since the SPF record is not configured for the subdomain, we can arbitrarily construct the subdomain, such as test.email-target.com, to send emails. 

<img width="300" alt="1688022986040" src="https://github.com/sunknighteric/Measurement_for_SPF_and_DMARC_2022/assets/32115816/1e30f2fc-a34e-4414-91ea-b34a8ab09901">

As shown in Figure (c), we can see that the SPF check result is none, which is the same as Figure (a). 

#### DMARC Using None Policy

We add a DMARC record as:

```
    Type:txt
    Host:_dmarc
    Value:v=DMARC1; p=none;
```

<img width="300" alt="1688023044017" src="https://github.com/sunknighteric/Measurement_for_SPF_and_DMARC_2022/assets/32115816/6035dada-cae2-4acb-b519-76430554d9af">

When policy p is set to none, even if the mail fails both SPF and DMARC check, the receiving server may still accept the mail, which is shown in Figure (d).

## SPF and DMARC Checking Results of Email Service Providers

Table below summarizes SPF and DMARC adoption change situation of thirty-five domains. Only one email provider (t-online.de) does not support SPF or DMARC. Since 2015, six domains have strengthen their SPF configuration policy. The policy for SPF is mostly configured as soft fail or hard fail, and only three are set as neutral. None of the domains uses the pass mechanism. In case of DMARC, compared with previous results, ten domains start to have DMARC configuration and still there are six domains do not support DMARC. Sixteen providers use testing mode with the none policy (e.g., gmail.com), seven use the quarantine policy, and six use the strictest reject policy.

For subdomains, only Mail.ru has set a hard fail SPF record for *.mail.ru, and only seven domains have configured the sp policy of DMARC to protect their subdomains.

| Provider |  SPF         | SPF | SPF | SPF Subdomain| SPF Subdomain | SPF Subdomain |DMARC|DMARC |DMARC |DMARC Subdomain|DMARC Subdomain |DMARC Subdomain |
| ----- | --------- | ----------- | ------- |--------- | ----------- | ------- |--------- | ----------- | ------- |--------- | ----------- | ------- |
| | 2015       | 2020  | 2022  | 2015       | 2020  | 2022  | 2015       | 2020  | 2022  | 2015       | 2020  | 2022  |
| gmail.com  | soft fail | soft fail | soft fail | N/A | N/A | -         | none   | reject     | none       | N/A | N/A | quarantine |
| yahoo.com  | neutral   | neutral   | neutral   | N/A | N/A | -         | reject | reject     | reject     | N/A | N/A | -          |
| outlook.com  | soft fail | soft fail | soft fail | N/A | N/A | -         | none   | none       | none       | N/A | N/A | quarantine |
| icloud.com  | soft fail | N/A       | soft fail | N/A | N/A | -         | none   | N/A        | quarantine | N/A | N/A | -          |
| hushmail.com  | soft fail | N/A       | hard fail | N/A | N/A | -         | -      | N/A        | quarantine | N/A | N/A | -          |
| lycos.com  | soft fail | N/A       | soft fail | N/A | N/A | -         | -      | N/A        | -          | N/A | N/A | -          |
| mail.com  | hard fail | N/A       | hard fail | N/A | N/A | -         | -      | N/A        | none       | N/A | N/A | quarantine |
| zoho.eu  | soft fail | hard fail | hard fail | N/A | N/A | -         | -      | reject     | reject     | N/A | N/A | reject     |
| mail.ru  | soft fail | soft fail | soft fail | N/A | N/A | hard fail | none   | reject     | reject     | N/A | N/A | -          |
| aol.com | soft fail | soft fail | soft fail | N/A | N/A | -         | reject | reject     | reject     | N/A | N/A | -          |
| qq.com   | soft fail | N/A       | hard fail | N/A | N/A | -         | none   | N/A        | quarantine | N/A | N/A | -          |
| me.com   | soft fail | N/A       | soft fail | N/A | N/A | -         | none   | N/A        | quarantine | N/A | N/A | -          |
| facebook.com  | hard fail | N/A       | hard fail | N/A | N/A | -         | reject | N/A        | reject     | N/A | N/A | -          |
| godaddy.com  | hard fail | N/A       | hard fail | N/A | N/A | -         | none   | N/A        | reject     | N/A | N/A | -          |
| yandex.com  | soft fail | N/A       | soft fail | N/A | N/A | -         | -      | N/A        | none       | N/A | N/A | -          |
| ovh.com  | neutral   | N/A       | soft fail | N/A | N/A | -         | -      | N/A        | none       | N/A | N/A | -          |
| daum.net  | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | -          | none       | N/A | N/A | -          |
| fastmail.com   | N/A       | neutral   | neutral   | N/A | N/A | neutral   | N/A    | none       | none       | N/A | N/A | none       |
| firemail.de    | N/A       | neutral   | hard fail | N/A | N/A | -         | N/A    | -          | -          | N/A | N/A | -          |
| freemail.hu   | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | -          | -          | N/A | N/A | -          |
| freenet.de    | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | -          | -          | N/A | N/A | -          |
| gmx.de   | N/A       | hard fail | hard fail | N/A | N/A | -         | N/A    | -          | none       | N/A | N/A | -          |
| hotmail.com   | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | none       | none       | N/A | N/A | -          |
| inbox.lv  | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | quarantine | quarantine | N/A | N/A | quarantine |
| interia.pl  | N/A       | hard fail | hard fail | N/A | N/A | -         | N/A    | -          | none       | N/A | N/A | -          |
| mail.de  | N/A       | neutral   | soft fail | N/A | N/A | -         | N/A    | none       | none       | N/A | N/A | -          |
| naver.com | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | -          | none       | N/A | N/A | -          |
| op.pl   | N/A       | hard fail | hard fail | N/A | N/A | -         | N/A    | -          | none       | N/A | N/A | -          |
| protonmail.com    | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | quarantine | quarantine | N/A | N/A | -          |
| runbox.com      | N/A       | hard fail | hard fail | N/A | N/A | -         | N/A    | none       | none       | N/A | N/A | -          |
| sapo.pt     | N/A       | soft fail | soft fail | N/A | N/A | -         | N/A    | -          | -          | N/A | N/A | -          |
| seznam.cz    | N/A       | neutral   | neutral   | N/A | N/A | -         | N/A    | none       | none       | N/A | N/A | -          |
| t-online.de     | N/A       | -         | -         | N/A | N/A | -         | N/A    | -          | -          | N/A | N/A | -          |
| tutanota.com    | N/A       | hard fail | hard fail | N/A | N/A | -         | N/A    | none       | quarantine | N/A | N/A | -          |
| web.de   | N/A       | hard fail | hard fail | N/A | N/A | -         | N/A    | -          | none       | N/A | N/A | quarantine |

