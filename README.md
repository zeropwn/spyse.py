# spyse.py
![Build Status](https://travis-ci.org/zeropwn/spyse.py.svg?branch=master)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/download/releases/3.0/)
[![GitHub license](https://img.shields.io/github/license/zeropwn/spyse.py.svg)](https://github.com/zeropwn/spyse.py/blob/master/LICENSE)
![](https://i.imgur.com/vpgzWEi.png)

Python API wrapper and command-line client for the tools hosted on spyse.com.

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
* ```-target```
* ```-param```

#### Optional Arguments
* ```-page```
* ```-apikey```
* ```--raw```

#### What is the param argument?

Spyse allows you to search their database for IPs, IP ranges, domain names, URLs, etc. The parameter argument is meant to specify the type of your input.

#### List of parameters
* ```cidr```
* ```domain```
* ```ip```
* ```page```
* ```url```
* ```hash```
* ```q```

#### Using search queries
Much like Shodan, Spyse allows you to use search queries. To do this, you must supply the "q" parameter. From there, it's as simple as supplying "org: Microsoft" as the target.
```bash
spyse -target "org: Microsoft" -param q --ssl-certificates
```

#### Searching for subdomains
```bash
spyse -target xbox.com -param domain --subdomains
```

#### Reverse IP Lookup
```bash
spyse -target 52.14.144.171 -param ip --domains-on-ip
```

#### Searching for SSL certificates
```bash
spyse -target hotmail.com -param domain --ssl-certificates
```
```bash
spyse -target "org: Microsoft" -param q --ssl-certificates
```
#### Getting all DNS records
```bash
spyse -target xbox.com -param domain --dns-all
```

#### Navigating multiple pages using your API key
```bash
export SPYSEKEY="yourkeyhere"
spyse -target xbox.com -param domain -apikey $SPYSEKEY -page 2 ---ssl-certificates
```
#### Piping to jq and aquatone
Initially when I decided to write this client I really wanted it to focus on flexibility within the command-line, which is why there is the ```--raw``` option. From there you can work with the raw JSON returned by the API.

```bash
spyse -target hackerone.com -param domain --dns-soa --raw | jq
```

[![asciicast](https://asciinema.org/a/253602.svg)](https://asciinema.org/a/253602)
```bash
spyse -target hackerone.com -param domain --subdomains --raw | aquatone
```
[![asciicast](https://asciinema.org/a/253650.svg)](https://asciinema.org/a/253650)

#### Other options
```
usage: spyse [-h] [-target TARGET] [-param PARAM] [-page PAGE]
             [-apikey APIKEY] [--raw] [--dns-ptr] [--dns-soa] [--dns-mx]
             [--dns-aaaa] [--dns-ns] [--dns-a] [--dns-txt] [--dns-all]
             [--domains-with-same-ns] [--domains-using-as-mx]
             [--domains-on-ip] [--domains-with-same-mx]
             [--domains-using-as-ns] [--download-dns-aaaa]
             [--download-dns-soa] [--download-dns-ns] [--download-dns-ptr]
             [--download-dns-mx] [--download-dns-a] [--download-dns-txt]
             [--download-dns-all] [--ip-port-lookup]
             [--ip-port-lookup-aggregate] [--ssl-certificates] [--subdomains]

Client for Spyse.com

optional arguments:
  -h, --help            show this help message and exit
  -target TARGET        target
  -param PARAM          parameter to use (ip, domain, cidr, url, hash)
  -page PAGE            page
  -apikey APIKEY        set the api key
  --raw                 show raw json
  --dns-ptr             show dns ptr records
  --dns-soa             show dns soa records
  --dns-mx              show dns mx records
  --dns-aaaa            show dns aaaa records
  --dns-ns              show dns ns records
  --dns-a               show dns a records
  --dns-txt             show dns txt records
  --dns-all             show all dns records
  --domains-with-same-ns
                        show domains with same ns
  --domains-using-as-mx
                        show domains using as mx
  --domains-on-ip       show domains on ip
  --domains-with-same-mx
                        show domains with same mx
  --domains-using-as-ns
                        show domains using as ns
  --download-dns-aaaa   download dns aaaa records
  --download-dns-soa    download dns soa records
  --download-dns-ns     download dns ns records
  --download-dns-ptr    download dns ptr records
  --download-dns-mx     download dns mx records
  --download-dns-a      download dns a records
  --download-dns-txt    download dns txt records
  --download-dns-all    download all dns records
  --ip-port-lookup      show ip port lookup
  --ip-port-lookup-aggregate
                        show ip port lookup aggregate
  --ssl-certificates    show ssl certificates associated with a target
  --subdomains          show subdomains

Usage: spyse -target <TARGET> -param <PARAM> --subdomains
```

## Using the library

#### Without API Key
```python
from spyse import spyse

s = spyse()
subdomains = s.subdomains("xbox.com", param="domain")
```

#### With API Key
```python
from spyse import spyse

# Using the API key allows us to go through multiple pages of results
s = spyse('API_TOKEN_GOES_HERE')
subdomains = s.subdomains_aggregate("xbox.com", param="domain", page=2)
```

#### Search using CIDR
```python
from spyse import spyse

s = spyse()
results = s.domains_on_ip("172.217.1.0/24", param="cidr")
```

#### Work with an existing file
```python
from spyse import spyse

s = spyse()
results = []

with open("domains.txt") as d:
    for line in d:
        # default value for param="domain", so we don't
        # need to specify here
        r = s.subdomains_aggregate(line)
        results.append(r)

print(results)
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

