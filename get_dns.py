import dns.resolver


"""Docs:
    This is a simple program that prints a website DNS info depending on a record type. Posible records:

        A Record: It is fundamental type of DNS record, here A stands for address. 
        It shows the IP address of the domain.

        AAAA Record: This is an IP address record, used to find the IP of the computer connected to the domain. 
        It is conceptually similar to A record but specifies only the IPv6 address of the server rather than IPv4.

        PTR Record: PTR stands for pointer record, used to translate IP addresses to the domain name or hostname. 
        It is used to reverse the DNS lookup.

        NS Record: Nameserver(NS) record gives information that which server is authoritative for the given domain i.e. which server has the actual DNS records. 
        Multiple NS records are possible for a domain including the primary and the backup name servers.

        MX Records: MX stands for Mail Exchanger record, which is a resource record that specifies the mail server which is responsible for accepting emails on behalf of the domain. 
        It has preference values according to the prioritizing mail if multiple mail servers are present for load balancing and redundancy.
            
        SOA Records: SOA stands for Start of Authority records, which is a type of resource record that contains information regarding the 
        administration of the zone especially related to zone transfers defined by the zone administrator.
        
        CNAME Record: CNAME stands for Canonical  Name record, which is used in mapping the domain name as an alias for the other domain. 
        It always points to another domain and never directly points to an IP."""

while True:
    rec_type = input("Record type (or type 'exit' to end) -> ")
    rec_type = rec_type.upper()

    if rec_type == 'A':
        source = input('Source address -> ')
        result = dns.resolver.query(source, 'A')

        for val in result:
            print('A Record :: ', val.to_text())
    elif rec_type == 'AAAA':
        source = input('Source address -> ')
        result = dns.resolver.query(source, 'AAAA')

        for val in result:
            print('AAAA Record :: ', val.to_text())
    elif rec_type == 'MX':
        source = input('Source address -> ')
        result = dns.resolver.query(source, 'MX')

        for val in result:
            print('MX Record :: ', val.to_text())
    elif rec_type == 'PTR':
        source = input('Source address (IPV4) -> ')
        result = dns.resolver.query(source, 'PTR')

        for val in result:
            print('PTR Record :: ', val.to_text())
    elif rec_type == 'NS':
        source = input('Source address -> ')
        result = dns.resolver.query(source, 'NS')

        for val in result:
            print('NS Record :: ', val.to_text())
    elif rec_type == 'SOA':
        source = input('Source address -> ')
        result = dns.resolver.query(source, 'SOA')

        for val in result:
            print('SOA Record :: ', val.to_text())
    elif rec_type == 'CNAME':
        source = input('Source address -> ')
        result = dns.resolver.query(source, 'CNAME')

        for val in result:
            print('CNAME Record :: ', val.target)
    elif rec_type == 'exit':
        break
