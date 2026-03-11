# Network Service Enumeration and Vulnerability Detection using Nmap

Author: Sakshi Singh

## Project Overview
This project demonstrates how network reconnaissance and vulnerability detection can be performed using Nmap. Network enumeration helps identify active hosts, open ports, and running services on a target system, which is an essential step in penetration testing and security assessments.

## Objective
The objectives of this project were:
- To perform network scanning using Nmap
- To identify open ports and active services
- To detect potential vulnerabilities in exposed services
- To understand how attackers gather information about target systems

## Tool Used
Primary Tool:
- Nmap (Network Mapper)

Nmap is a widely used open-source tool for network discovery and security auditing.

## Methodology

The following steps were performed during the scan:

1. Installed and configured Nmap.
2. Identified the target host or system.
3. Performed host discovery to determine if the target was active.
4. Conducted port scanning to detect open ports.
5. Identified services and versions running on open ports.
6. Performed vulnerability detection using Nmap scripts.
7. Analyzed the scan results and identified potential security risks.

## Types of Scans Performed

- Host Discovery Scan
- TCP Port Scan
- Service Version Detection
- OS Detection
- Vulnerability Scan using Nmap Scripting Engine (NSE)

## Example Findings

The scan identified several open ports and services that could potentially be exploited if not properly secured.

Examples include:
- Open HTTP service
- Open SSH service
- Running services with identifiable versions
- Possible outdated software versions

These findings highlight the importance of monitoring exposed services and keeping systems updated.

## Security Recommendations

To improve the security posture of the system, the following recommendations are suggested:

- Close unnecessary open ports.
- Restrict access to critical services using firewalls.
- Regularly update and patch software and services.
- Disable unused services.
- Implement network monitoring and intrusion detection systems.

## Conclusion

This project demonstrates how Nmap can be used to perform network enumeration and identify potential security risks. Network scanning is an important step in vulnerability assessment and helps organizations understand their attack surface and improve their overall security posture.
