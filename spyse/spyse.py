#!/usr/bin/python3

import requests

class spyse:

	API_URL = "https://api.spyse.com/v1"

	# Available methods on Spyse API.
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
		"download_dns_ptr": "/download-dns-ptr",
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

	# Parameter arguments supported by the Spyse API
	API_TARGET_PARAMS = [
		'cidr',
		'domain',
		'sdword',
		'ip',
		'page',
		'url',
		'hash',
		'q'
	]

	# Default value for API key is False so that you
	# don't have to specify that you don't want to use
	# one
	def __init__(self, apikey=False):
		self.apikey = apikey

	# Provides information about PTR Records, total count of records
	# in DB, related information about IPs (ASN, country, organization,
	# OSH), related information about domains (current IP, subdomain 
	# count).
	def dns_ptr(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_PTR'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about SOA Records and total count of records in DB.	
	def dns_soa(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_SOA'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about MX Records, total count of records in DB,
	# related information about IPs (ASN, country, organization) and
	# domains (current IP, subdomain count).
	def dns_mx(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_MX'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about AAAA Records, total count of records in DB,
	# related information about domains (current IP, subdomain count).
	def dns_aaaa(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_AAAA'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about NS Records, total count of records in DB,
	# related information about IPs (ASN, country, organization) and domains
	# (current IP, subdomain count).
	def dns_ns(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_NS'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about A Records, total count of records in DB,
	# related information about IPs (ASN, country, organization) and domains
	# (current IP, subdomain count).
	def dns_a(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_A'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about TXT Records and total count of records in DB.
	def dns_txt(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['DNS_TXT'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about domains with same NS records.
	def domains_with_same_ns(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_with_same_ns'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about domains that used provided domain as mail server.
	def domains_using_as_mx(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_using_as_mx'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about domains on same IP/CIDR. If domain is provided,
	# method will return domains that have matching IPs. If two or more parameters
	# are provided, method will return domains satisfying each of the conditions.
	def domains_on_ip(self, target, param='ip', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_on_ip'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about domains with same MX records.
	def domains_with_same_mx(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_with_same_mx'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides information about domains that used provided domain as name server.
	def domains_using_as_ns(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_using_as_ns'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Downloading AAAA records in .txt or .tsv format
	def download_dns_aaaa(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_aaaa'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading SOA records in .txt or .tsv format.
	def download_dns_soa(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_soa'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading NS records in .txt or .tsv format
	def download_dns_ns(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_ns'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading MX records in .txt or .tsv format.
	def download_dns_mx(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_mx'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading PTR records in .txt or .tsv format.
	def download_dns_ptr(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_ptr'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading A records in .txt or .tsv format.
	def download_dns_a(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_a'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading TXT records in .txt or .tsv format.
	def download_dns_txt(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_dns_txt'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading domains with same MX records in .txt or .tsv format.
	def download_domains_with_same_mx(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_domains_with_same_mx'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading domains on same IP in .txt or .tsv format.
	def download_domains_on_ip(self, target, param='ip', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_domains_on_ip'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading domains with same NS records in .txt or .tsv format.
	def download_domains_with_same_ns(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_domains_with_same_ns'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading domains using as NS in .txt or .tsv format.
	def download_domains_using_as_ns(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_domains_using_as_ns'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Downloading domains using as MX in .txt or .tsv format.
	def download_domains_using_as_mx(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['download_domains_using_as_mx'],
			self.apikey,
			param,
			target,
			page
		))
		return r.text

	# Provides aggregate information about IP port lookup.
	def ip_port_lookup_aggregate(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ip_port_lookup_aggregate'],
			self.apikey,
			'q',
			target,
			page
		))
		return r.json()

	# Provides list of IP port lookup indexed by IP.
	def ip_port_lookup(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ip_port_lookup'],
			self.apikey,
			'q',
			target,
			page
		))
		return r.json()

	# Provides list of SSL certificates.
	def ssl_certificates(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		if param == 'domain':
			param = 'url'
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ssl_certificates'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns raw ssl certificate.
	def ssl_certificate_raw(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		if param == 'domain':
			param = 'url'
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ssl_certificate_raw'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides aggregate information about SSL certificates by provided query.
	def ssl_certificates_aggregate(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ssl_certificates_aggregate'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Provides all information about SSL certificate by hash.
	def ssl_certificate(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ssl_certificate'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns SSL certificate's public key.
	def ssl_certificate_public_key(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ssl_certificate_public_key'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns SSL certificate's JSON.
	def ssl_certificate_json(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['ssl_certificate_json'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns a list of subdomains of provided domain.
	def subdomains(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['subdomains'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns aggregate information by domain: total count of subdomains,
	# list of IPs of subdomains and subdomain count on every IP, list of AS
	# numbers and subdomain count on every AS number, list of countries and
	# subdomain count from it, list of CIDRs /24, /16 and subdomain list on
	# every CIDR.
	def subdomains_aggregate(self, target, param='domain', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['subdomains_aggregate'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns a list of domains that starts with provided sdword.
	def domains_starts_with(self, target, param='sdword', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_starts_with'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()

	# Returns aggregate information by sdword: total count of domains that starts
	# with provided sdword, list of IPs of subdomains and subdomain count on every IP,
	# list of AS numbers and subdomain count on every AS number, list of countries and
	# subdomain count from it, list of CIDRs /24, /16 and subdomain list on every CIDR.
	def domains_starts_with_aggregate(self, target, param='sdword', page=1):
		if param not in self.API_TARGET_PARAMS:
			return "Invalid parameter."
		r = requests.get("{}/{}?api_token={}&{}={}&page={}".format(
			self.API_URL,
			self.API_METHODS['domains_starts_with_aggregate'],
			self.apikey,
			param,
			target,
			page
		))
		return r.json()
