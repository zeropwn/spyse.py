# spyse.py
![Build Status](https://travis-ci.org/zeropwn/spyse.py.svg?branch=master)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/download/releases/3.0/)
[![GitHub license](https://img.shields.io/github/license/zeropwn/spyse.py.svg)](https://github.com/zeropwn/spyse.py/blob/master/LICENSE)
![](https://i.imgur.com/fX2NncJ.jpg)

Python API wrapper for the tools hosted on spyse.com.


"Spyse is a developer of complete DAAS (Data-As-A-Service) solutions for Internet security professionals, corporate and remote system administrators, SSL / TLS encryption certificate providers, data centers and business analysts. All Spyse online solutions are represented by thematic services that have a single platform for collecting, processing and aggregating information."
\- spyse.com

Supports the following APIs:
- [DNStable](https://dnstable.com)
- [FindSubdomains](https://findsubdomains.com)
- [CertDB](https://certdb.com)
- [ASlookup](https://aslookup.com)
- [PortMap](https://portmap.com)
- [DomainsDB](https://domainsdb.org)


#### NOTE: This API is currently under active development.

## Installation

```bash
pip3 install spyse.py
```

## Using the client

#### Required Arguments
* -target
* -param

#### Optional Arguments
* -page
* -apikey
* --raw

#### The deal with parameters

Spyse allows you to search their database for IPs, IP ranges, domain names, URLs, etc. The parameter argument is meant to specify the type of your input.


#### Example usages

```bash
spyse -target xbox.com -param domain --subdomains
spyse -target 127.0.0.1/24 -param cidr --domains-on-ip
spyse -target hotmail.com -param url --ssl-certificates
spyse -target google.com -param domain --dns-all
spyse -target xbox.com -param domain -apikey <APIKEY> -page 2 --ssl-certificates --raw
```


## Using the library

#### Without API Key
```python
from pprint import pprint
from spyse import spyse

s = spyse()
pprint(s.subdomains_aggregate("xbox.com", param="domain"))
```

#### With API Key
```python
from spyse import spyse

s = spyse('API_TOKEN_GOES_HERE')
pprint(s.subdomains_aggregate("xbox.com", param="domain"))
```

#### Search using CIDR
```python
from spyse import spyse
from pprint import pprint

s = spyse()
pprint(s.domains_on_ip("172.217.1.0/24", param="cidr"))
```

#### Fetch subdomains
```python
from spyse import spyse

TARGET = "TARGET_HOST_HERE"

s = spyse()
data = s.subdomains_aggregate(TARGET, param="domain")['cidr']
keys = data.keys()
for key in keys:
	domains = data[key]['results']
	for d in domains:
		domain = d['data']['domains']
		if len(domain) > 1:
			for i in domain:
				print(i)
		else:
			print(domain[0])
```


## Available Methods

All of the methods listed on https://api-doc.spyse.com/

```python
	API_METHODS = {
		"DNS_PTR": "/dns-ptr",
		"DNS_SOA": "/dns-soa",
		"DNS_MX": "/dns-mx",
		"DNS_AAAA": "/dns-aaaa",
		"DNS_NS": "/dns-ns",
		"DNS_A": "/dns-a",
		"DNS_TXT": "/dns-txt",
		"domains_with_same_ns": "/domains-with-same-ns",
		"domains_using_as_mx": "/domains-using-as-mx",
		"domains_on_ip": "/domains-on-ip",
		"domains_with_same_mx": "/domains-with-same-mx",
		"domains_using_as_ns": "/domains-using-as-ns",
		"download_dns_aaaa": "/download-dns-aaaa",
		"download_dns_soa": "/download-dns-soa",
		"download_dns_ns": "/download-dns-ns",
		"download_dns_ptr": "/download-ns-ptr",
		"download_dns_mx": "/download-dns-mx",
		"download_dns_a": "/download-dns-a",
		"download_dns_txt": "/download-dns-txt",
		"download_domains_with_same_mx": "/download-domains-with-same-mx",
		"download_domains_on_ip": "/download-domains-on-ip",
		"download_domains_with_same_ns": "/download-domains-with-same-ns",
		"download_domains_using_as_ns": "/download-domains-using-as-ns",
		"download_domains_using_as_mx": "/download-domains-using-as-mx",
		"ip_port_lookup_aggregate": "/ip-port-lookup-aggregate",
		"ip_port_lookup": "/ip-port-lookup",
		"ssl_certificates": "/ssl-certificates",
		"ssl_certificate_raw": "/ssl-certificate-raw",
		"ssl_certificates_aggregate": "ssl-certificates-aggregate",
		"ssl_certificate": "/ssl-certificate",
		"ssl_certificate_public_key": "/ssl-certificate-public-key",
		"ssl_certificate_json": "/ssl-certificate-json",
		"subdomains": "/subdomains",
		"subdomains_aggregate": "/subdomains-aggregate",
		"domains_starts_with": "/domains-starts-with",
		"domains_starts_with_aggregate": "/domains-starts-with-aggregate"
	}
  ```

