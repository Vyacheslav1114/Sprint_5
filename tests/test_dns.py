# tests/test_dns.py
import socket

def test_dns_resolves():
    name = "stellarburgers.education-services.ru"
    ip = socket.gethostbyname(name)
    print("Resolved IP for", name, "->", ip)
    assert ip is not None and ip != ""
