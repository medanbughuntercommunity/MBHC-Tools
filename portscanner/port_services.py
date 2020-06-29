import json

services_data = '[{"portid":"tcpmux","portdefaultnumber":1,\
                        "portdesc":"TCP Port Service Multiplexer","portprotocol":"tcp"},\
                    {"portid":"echo","portdefaultnumber":7,\
                        "portdesc":"Echo","portprotocol":"tcp"},\
                    {"portid":"discard","portdefaultnumber":9,\
                        "portdesc":"Sink Null","portprotocol":"tcp"},\
                    {"portid":"systat","portdefaultnumber":11,\
                        "portdesc":"Active Users","portprotocol":"tcp"},\
                    {"portid":"daytime","portdefaultnumber":13,\
                        "portdesc":"Daytime","portprotocol":"tcp"},\
                    {"portid":"netstat","portdefaultnumber":15,\
                        "portdesc":"Netstat","portprotocol":"tcp"},\
                    {"portid":"qotd","portdefaultnumber":17,\
                        "portdesc":"Quote of The Day","portprotocol":"tcp"},\
                    {"portid":"chargen","portdefaultnumber":19,\
                        "portdesc":"Character Generator","portprotocol":"tcp"},\
                    {"portid":"ftp-data","portdefaultnumber":20,\
                        "portdesc":"File Transfer Default Data","portprotocol":"tcp"},\
                    {"portid":"ftp","portdefaultnumber":21,\
                        "portdesc":"File Transfer Control","portprotocol":"tcp"},\
                    {"portid":"ssh","portdefaultnumber":22,\
                        "portdesc":"Secure Shell Login","portprotocol":"tcp"},\
                    {"portid":"telnet","portdefaultnumber":23,\
                        "portdesc":"Telnet","portprotocol":"tcp"},\
                    {"portid":"smtp","portdefaultnumber":25,\
                        "portdesc":"Simple Mail Transfer","portprotocol":"tcp"},\
                    {"portid":"time","portdefaultnumber":37,\
                        "portdesc":"Time Server","portprotocol":"tcp"},\
                    {"portid":"whois","portdefaultnumber":43,\
                        "portdesc":"Whois","portprotocol":"tcp"},\
                    {"portid":"tacacs","portdefaultnumber":49,\
                        "portdesc":"Login Host Protocol","portprotocol":"tcp"},\
                    {"portid":"domain","portdefaultnumber":53,\
                        "portdesc":"Domain Name Server","portprotocol":"tcp"},\
                    {"portid":"bootps","portdefaultnumber":67,\
                        "portdesc":"DHCP/Bootstrap Protocol Server","portprotocol":"tcp"},\
                    {"portid":"bootpc","portdefaultnumber":68,\
                        "portdesc":"DHCP/Bootstrap Protocol Client","portprotocol":"tcp"},\
                    {"portid":"tftp","portdefaultnumber":69,\
                        "portdesc":"Trivial File Transfer","portprotocol":"tcp"},\
                    {"portid":"gopher","portdefaultnumber":70,\
                        "portdesc":"Internet Gopher","portprotocol":"tcp"},\
                    {"portid":"finger","portdefaultnumber":79,\
                        "portdesc":"Finger","portprotocol":"tcp"},\
                    {"portid":"http","portdefaultnumber":80,\
                        "portdesc":"World Wide Web HTTP","portprotocol":"tcp"},\
                    {"portid":"kerberos","portdefaultnumber":88,\
                        "portdesc":"Kerberos","portprotocol":"tcp"},\
                    {"portid":"iso-tsap","portdefaultnumber":102,\
                        "portdesc":"Part Of ISODE","portprotocol":"tcp"},\
                    {"portid":"acr-nema","portdefaultnumber":104,\
                        "portdesc":"ACR-NEMA Digital Imag. & Comm. 300","portprotocol":"tcp"},\
                    {"portid":"pop3","portdefaultnumber":110,\
                        "portdesc":"Post Office Protocol v3","portprotocol":"tcp"},\
                    {"portid":"sunrpc","portdefaultnumber":111,\
                        "portdesc":"SUN Remote Procedure Call","portprotocol":"tcp"},\
                    {"portid":"auth","portdefaultnumber":113,\
                        "portdesc":"Authentication Service","portprotocol":"tcp"},\
                    {"portid":"nntp","portdefaultnumber":119,\
                        "portdesc":"Network News Transfer Protocol","portprotocol":"tcp"},\
                    {"portid":"ntp","portdefaultnumber":123,\
                        "portdesc":"Network Time Protocol","portprotocol":"tcp"},\
                    {"portid":"msrpc","portdefaultnumber":135,\
                        "portdesc":"Microsoft RPC Services","portprotocol":"tcp"},\
                    {"portid":"netbios-ns","portdefaultnumber":137,\
                        "portdesc":"NETBIOS Name Service","portprotocol":"tcp"},\
                    {"portid":"netbios-dgm","portdefaultnumber":138,\
                        "portdesc":"NETBIOS Datagram Service","portprotocol":"tcp"},\
                    {"portid":"netbios-ssn","portdefaultnumber":139,\
                        "portdesc":"NETBIOS Session Service","portprotocol":"tcp"},\
                    {"portid":"imap2","portdefaultnumber":143,\
                        "portdesc":"Internet Message Access Protocol","portprotocol":"tcp"},\
                    {"portid":"snmp","portdefaultnumber":161,\
                        "portdesc":"Simple Net MGMT Proto","portprotocol":"tcp"},\
                    {"portid":"snmp-trap","portdefaultnumber":162,\
                        "portdesc":"SNMP Traps","portprotocol":"tcp"},\
                    {"portid":"cmip-man","portdefaultnumber":163,\
                        "portdesc":"CMIP/TCP Manager","portprotocol":"tcp"},\
                    {"portid":"cmip-agent","portdefaultnumber":164,\
                        "portdesc":"CMIP/TCP Agent","portprotocol":"tcp"},\
                    {"portid":"mailq","portdefaultnumber":174,\
                        "portdesc":"MailQ","portprotocol":"tcp"},\
                    {"portid":"xdmcp","portdefaultnumber":177,\
                        "portdesc":"X Display Manager Control Protocol","portprotocol":"tcp"},\
                    {"portid":"bgp","portdefaultnumber":179,\
                        "portdesc":"Border Gateway Protocol","portprotocol":"tcp"},\
                    {"portid":"smux","portdefaultnumber":199,\
                        "portdesc":"SNMP Unix Multiplexer","portprotocol":"tcp"},\
                    {"portid":"qmtp","portdefaultnumber":209,\
                        "portdesc":"Quick Mail Transfer Protocol","portprotocol":"tcp"},\
                    {"portid":"z3950","portdefaultnumber":210,\
                        "portdesc":"NISO Z39.50 database","portprotocol":"tcp"},\
                    {"portid":"ipx","portdefaultnumber":213,\
                        "portdesc":"IPX","portprotocol":"tcp"},\
                    {"portid":"ptp-event","portdefaultnumber":319,\
                        "portdesc":"PTP-EVENT","portprotocol":"tcp"},\
                    {"portid":"ptp-general","portdefaultnumber":320,\
                        "portdesc":"IPX","portprotocol":"tcp"},\
                    {"portid":"pawserv","portdefaultnumber":345,\
                        "portdesc":"Perf Analysis Workbench","portprotocol":"tcp"},\
                    {"portid":"zserv","portdefaultnumber":346,\
                        "portdesc":"Zebra Server","portprotocol":"tcp"},\
                    {"portid":"rpc2portmap","portdefaultnumber":369,\
                        "portdesc":"Coda Portmapper","portprotocol":"tcp"},\
                    {"portid":"codaauth2","portdefaultnumber":370,\
                        "portdesc":"IPX","portprotocol":"tcp"},\
                    {"portid":"clearcase","portdefaultnumber":371,\
                        "portdesc":"Clearcase","portprotocol":"tcp"},\
                    {"portid":"ldap","portdefaultnumber":389,\
                        "portdesc":"Lightweight Directory Access Protocol","portprotocol":"tcp"},\
                    {"portid":"svrloc","portdefaultnumber":427,\
                        "portdesc":"Server Location","portprotocol":"tcp"},\
                    {"portid":"https","portdefaultnumber":443,\
                        "portdesc":"World Wide Web HTTPS","portprotocol":"tcp"},\
                    {"portid":"snpp","portdefaultnumber":444,\
                        "portdesc":"Simple Network Paging Protocol","portprotocol":"tcp"},\
                    {"portid":"microsoft-ds","portdefaultnumber":445,\
                        "portdesc":"Microsoft Naked CIFS","portprotocol":"tcp"},\
                    {"portid":"kpasswd","portdefaultnumber":464,\
                        "portdesc":"Kerberos","portprotocol":"tcp"},\
                    {"portid":"submissions","portdefaultnumber":465,\
                        "portdesc":"Submissions over TLS","portprotocol":"tcp"},\
                    {"portid":"saft","portdefaultnumber":487,\
                        "portdesc":"Simple Asynchronous File Transfer","portprotocol":"tcp"},\
                    {"portid":"isakmp","portdefaultnumber":500,\
                        "portdesc":"IPSEC Key Management","portprotocol":"tcp"},\
                    {"portid":"rtsp","portdefaultnumber":554,\
                        "portdesc":"Real Time Stream Control Protocol","portprotocol":"tcp"},\
                    {"portid":"nqs","portdefaultnumber":607,\
                        "portdesc":"Network Queuing System","portprotocol":"tcp"},\
                    {"portid":"asf-rmcp","portdefaultnumber":623,\
                        "portdesc":"IPX","portprotocol":"tcp"},\
                    {"portid":"qmqp","portdefaultnumber":628,\
                        "portdesc":"IPX","portprotocol":"tcp"},\
                    {"portid":"ipp","portdefaultnumber":631,\
                        "portdesc":"IPX","portprotocol":"tcp"},\
                    {"portid":"exec","portdefaultnumber":512,\
                        "portdesc":"COMSAT","portprotocol":"tcp"},\
                    {"portid":"login","portdefaultnumber":513,\
                        "portdesc":"BSD rlogind","portprotocol":"tcp"},\
                    {"portid":"shell","portdefaultnumber":514,\
                        "portdesc":"CMD Syslog","portprotocol":"tcp"},\
                    {"portid":"printer","portdefaultnumber":515,\
                        "portdesc":"Line Printer Spooler","portprotocol":"tcp"},\
                    {"portid":"talk","portdefaultnumber":517,\
                        "portdesc":"Talk","portprotocol":"tcp"},\
                    {"portid":"ntalk","portdefaultnumber":518,\
                        "portdesc":"Talk Daemon","portprotocol":"tcp"},\
                    {"portid":"efs","portdefaultnumber":520,\
                        "portdesc":"Local Routing Process","portprotocol":"tcp"},\
                    {"portid":"route","portdefaultnumber":520,\
                        "portdesc":"Router Routed --RIP","portprotocol":"udp"},\
                    {"portid":"gdomap","portdefaultnumber":538,\
                        "portdesc":"GDO MAP","portprotocol":"tcp"},\
                    {"portid":"uucp","portdefaultnumber":540,\
                        "portdesc":"UUCP Daemon","portprotocol":"tcp"},\
                    {"portid":"klogin","portdefaultnumber":543,\
                        "portdesc":"Kerberized rlogind","portprotocol":"tcp"},\
                    {"portid":"kshell","portdefaultnumber":544,\
                        "portdesc":"Kerberized rsh","portprotocol":"tcp"},\
                    {"portid":"dhcpv6-client","portdefaultnumber":546,\
                        "portdesc":"DHCP v6 Client","portprotocol":"udp"},\
                    {"portid":"dhcpv6-server","portdefaultnumber":547,\
                        "portdesc":"DHCP v6 Server","portprotocol":"udp"},\
                    {"portid":"afpovertcp","portdefaultnumber":548,\
                        "portdesc":"AFP Over TCP","portprotocol":"tcp"},\
                    {"portid":"nntps","portdefaultnumber":563,\
                        "portdesc":"NNTP Over SSL","portprotocol":"tcp"},\
                    {"portid":"submission","portdefaultnumber":587,\
                        "portdesc":"Submission","portprotocol":"tcp"},\
                    {"portid":"ldaps","portdefaultnumber":636,\
                        "portdesc":"LDAP Over SSL","portprotocol":"tcp"},\
                    {"portid":"tinc","portdefaultnumber":655,\
                        "portdesc":"TINC Control Port","portprotocol":"tcp"},\
                    {"portid":"silc","portdefaultnumber":706,\
                        "portdesc":"Secure Internet Live Conferencing","portprotocol":"tcp"},\
                    {"portid":"kerberos-adm","portdefaultnumber":749,\
                        "portdesc":"Kerberos kadmin","portprotocol":"tcp"},\
                    {"portid":"domain-s","portdefaultnumber":853,\
                        "portdesc":"DNS Over TLS","portprotocol":"tcp"},\
                    {"portid":"ftps-data","portdefaultnumber":989,\
                        "portdesc":"FTP Over SSL (Data)","portprotocol":"tcp"},\
                    {"portid":"ftps","portdefaultnumber":990,\
                        "portdesc":"FTP Over SSL","portprotocol":"tcp"},\
                    {"portid":"telnets","portdefaultnumber":992,\
                        "portdesc":"Telnet Over SSL","portprotocol":"tcp"},\
                    {"portid":"imaps","portdefaultnumber":993,\
                        "portdesc":"IMAP Over SSL","portprotocol":"tcp"},\
                    {"portid":"pop3s","portdefaultnumber":995,\
                        "portdesc":"POP-3 Over SSL","portprotocol":"tcp"},\
                    {"portid":"socks","portdefaultnumber":1080,\
                        "portdesc":"SOCKS Proxy Server","portprotocol":"tcp"},\
                    {"portid":"proofd","portdefaultnumber":1093,\
                        "portdesc":"PROOFD","portprotocol":"tcp"},\
                    {"portid":"rootd","portdefaultnumber":1094,\
                        "portdesc":"ROOTD","portprotocol":"tcp"},\
                    {"portid":"openvpn","portdefaultnumber":1194,\
                        "portdesc":"OpenVPN","portprotocol":"tcp"},\
                    {"portid":"rmiregistry","portdefaultnumber":1099,\
                        "portdesc":"Java RMI Registry","portprotocol":"tcp"},\
                    {"portid":"lotusnote","portdefaultnumber":1352,\
                        "portdesc":"Lotus Note","portprotocol":"tcp"},\
                    {"portid":"ms-sql-s","portdefaultnumber":1433,\
                        "portdesc":"Microsoft SQL Server","portprotocol":"tcp"},\
                    {"portid":"ms-sql-m","portdefaultnumber":1434,\
                        "portdesc":"Microsoft SQL Monitor","portprotocol":"tcp"},\
                    {"portid":"ingreslock","portdefaultnumber":1524,\
                        "portdesc":"Ingres Lock","portprotocol":"tcp"},\
                    {"portid":"datametrics","portdefaultnumber":1645,\
                        "portdesc":"Old Radius","portprotocol":"tcp"},\
                    {"portid":"sa-msg-port","portdefaultnumber":1646,\
                        "portdesc":"Old Radius Accounting","portprotocol":"tcp"},\
                    {"portid":"kermit","portdefaultnumber":1649,\
                        "portdesc":"Kermit","portprotocol":"tcp"},\
                    {"portid":"groupwise","portdefaultnumber":1677,\
                        "portdesc":"Groupwise","portprotocol":"tcp"},\
                    {"portid":"l2f","portdefaultnumber":1701,\
                        "portdesc":"L2TP","portprotocol":"tcp"},\
                    {"portid":"radius","portdefaultnumber":1812,\
                        "portdesc":"Radius","portprotocol":"tcp"},\
                    {"portid":"radius-acct","portdefaultnumber":1813,\
                        "portdesc":"Radius Accounting","portprotocol":"tcp"},\
                    {"portid":"cisco-sccp","portdefaultnumber":2000,\
                        "portdesc":"Cisco SCCP","portprotocol":"tcp"},\
                    {"portid":"nfs","portdefaultnumber":2049,\
                        "portdesc":"Network File System","portprotocol":"tcp"},\
                    {"portid":"gnunet","portdefaultnumber":2086,\
                        "portdesc":"GNUnet","portprotocol":"tcp"},\
                    {"portid":"rtcm-sc104","portdefaultnumber":2101,\
                        "portdesc":"RTCM SC-104 IANA","portprotocol":"tcp"},\
                    {"portid":"gsigatekeeper","portdefaultnumber":2119,\
                        "portdesc":"GSI gatekeeper","portprotocol":"tcp"},\
                    {"portid":"gris","portdefaultnumber":2135,\
                        "portdesc":"Grid Resource Information Server","portprotocol":"tcp"},\
                    {"portid":"cvspserver","portdefaultnumber":2401,\
                        "portdesc":"CVS Client/Server Operations","portprotocol":"tcp"},\
                    {"portid":"mysql","portdefaultnumber":3306,\
                        "portdesc":"MySQL","portprotocol":"tcp"},\
                    {"portid":"ms-wbt-server","portdefaultnumber":3389,\
                        "portdesc":"Microsoft Remote Display Protocol","portprotocol":"tcp"},\
                    {"portid":"nut","portdefaultnumber":3493,\
                        "portdesc":"Network UPS Tool","portprotocol":"tcp"},\
                    {"portid":"svn","portdefaultnumber":3690,\
                        "portdesc":"Subversion Protocol","portprotocol":"tcp"},\
                    {"portid":"sysrq","portdefaultnumber":4094,\
                        "portdesc":"Sysrq Daemon","portprotocol":"tcp"},\
                    {"portid":"remctl","portdefaultnumber":4373,\
                        "portdesc":"Remote Authenticated Command Service","portprotocol":"tcp"},\
                    {"portid":"ipsec-nat-t","portdefaultnumber":4500,\
                        "portdesc":"IPsec NAT-Traversal","portprotocol":"tcp"},\
                    {"portid":"radmin-port","portdefaultnumber":4899,\
                        "portdesc":"RAdmin Port","portprotocol":"tcp"},\
                    {"portid":"xmpp-client","portdefaultnumber":5222,\
                        "portdesc":"Jabber Client Connection","portprotocol":"tcp"},\
                    {"portid":"xmpp-server","portdefaultnumber":5269,\
                        "portdesc":"Jabber Server Connection","portprotocol":"tcp"},\
                    {"portid":"mdns","portdefaultnumber":5353,\
                        "portdesc":"Multicast DNS","portprotocol":"tcp"},\
                    {"portid":"postgresql","portdefaultnumber":5432,\
                        "portdesc":"PostgrSQL","portprotocol":"tcp"},\
                    {"portid":"x11","portdefaultnumber":6000,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-1","portdefaultnumber":6001,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-2","portdefaultnumber":6002,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-3","portdefaultnumber":6003,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-4","portdefaultnumber":6004,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-5","portdefaultnumber":6005,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-6","portdefaultnumber":6006,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"x11-7","portdefaultnumber":6007,\
                        "portdesc":"X Window System","portprotocol":"tcp"},\
                    {"portid":"gnutella-svc","portdefaultnumber":6346,\
                        "portdesc":"GNUtella SVC","portprotocol":"tcp"},\
                    {"portid":"gnutella-rtr","portdefaultnumber":6347,\
                        "portdesc":"GNUtella RTR","portprotocol":"tcp"},\
                    {"portid":"mysql-proxy","portdefaultnumber":6446,\
                        "portdesc":"MySQL Proxy","portprotocol":"tcp"},\
                    {"portid":"ircs-u","portdefaultnumber":6697,\
                        "portdesc":"IRC Via TLS/SSL","portprotocol":"tcp"},\
                    {"portid":"afs3-fileserver","portdefaultnumber":7000,\
                        "portdesc":"File Server","portprotocol":"tcp"},\
                    {"portid":"afs3-callback","portdefaultnumber":7001,\
                        "portdesc":"Callback to Cache Managers","portprotocol":"tcp"},\
                    {"portid":"afs3-prserver","portdefaultnumber":7002,\
                        "portdesc":"Users & Groups Database","portprotocol":"tcp"},\
                    {"portid":"afs3-vlserver","portdefaultnumber":7003,\
                        "portdesc":"Volume Location Database","portprotocol":"tcp"},\
                    {"portid":"afs3-kaserver","portdefaultnumber":7004,\
                        "portdesc":"AFS/Kerberos Authentication","portprotocol":"tcp"},\
                    {"portid":"afs3-volser","portdefaultnumber":7005,\
                        "portdesc":"Volume Management Server","portprotocol":"tcp"},\
                    {"portid":"afs3-errors","portdefaultnumber":7006,\
                        "portdesc":"Error Interpretation Service","portprotocol":"tcp"},\
                    {"portid":"afs3-bos","portdefaultnumber":7007,\
                        "portdesc":"Basic Overseer Process","portprotocol":"tcp"},\
                    {"portid":"afs3-update","portdefaultnumber":7008,\
                        "portdesc":"Server-to-Server Updater","portprotocol":"tcp"},\
                    {"portid":"afs3-rmtsys","portdefaultnumber":7009,\
                        "portdesc":"Remote Cache Manager Service","portprotocol":"tcp"},\
                    {"portid":"font-service","portdefaultnumber":7100,\
                        "portdesc":"X Font Service","portprotocol":"tcp"},\
                    {"portid":"http-alt","portdefaultnumber":8080,\
                        "portdesc":"WWW Caching Service","portprotocol":"tcp"},\
                    {"portid":"xmms2","portdefaultnumber":9667,\
                        "portdesc":"Cross-Platform Music Multiplexing System","portprotocol":"tcp"},\
                    {"portid":"nbd","portdefaultnumber":10809,\
                        "portdesc":"Linux Network Block Device","portprotocol":"tcp"},\
                    {"portid":"zabbix-agent","portdefaultnumber":10050,\
                        "portdesc":"Zabbix Agent","portprotocol":"tcp"},\
                    {"portid":"zabbix-trapper","portdefaultnumber":10051,\
                        "portdesc":"Zabbix Trapper","portprotocol":"tcp"},\
                    {"portid":"hkp","portdefaultnumber":11371,\
                        "portdesc":"OpenPGP HTTP Keyserver","portprotocol":"tcp"},\
                    {"portid":"db-lsp","portdefaultnumber":17500,\
                        "portdesc":"Dropbox LanSync Protocol","portprotocol":"tcp"},\
                    {"portid":"webmin","portdefaultnumber":10000,\
                        "portdesc":"Webmin","portprotocol":"tcp"},\
                    {"portid":"kerberos4","portdefaultnumber":750,\
                        "portdesc":"Kerberos (Server)","portprotocol":"tcp"},\
                    {"portid":"kerberos-master","portdefaultnumber":751,\
                        "portdesc":"Kerberos Authentication","portprotocol":"tcp"},\
                    {"portid":"passwd-server","portdefaultnumber":752,\
                        "portdesc":"Kerberos passwd server","portprotocol":"udp"},\
                    {"portid":"krb-prop","portdefaultnumber":754,\
                        "portdesc":"Kerberos Slave Propagation","portprotocol":"tcp"},\
                    {"portid":"ircd","portdefaultnumber":6667,\
                        "portdesc":"Internet Relay Chat","portprotocol":"tcp"},\
                    {"portid":"git","portdefaultnumber":9418,\
                        "portdesc":"GIT Version Control System","portprotocol":"tcp"},\
                    {"portid":"vnc","portdefaultnumber":5900,\
                        "portdesc":"Virtual Network Computer Display","portprotocol":"tcp"}\
                        ]'

services_array = json.loads(services_data)