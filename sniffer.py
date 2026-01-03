from scapy.all import sniff, IP, TCP, UDP, ICMP

ACTIVE_IFACE = r"\Device\NPF_{EAB06D23-2F23-44FB-9E58-A623B31F8BAA}"

def process_packet(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst

        if TCP in pkt:
            proto = "TCP"
            info = f"{pkt[TCP].sport} → {pkt[TCP].dport}"
        elif UDP in pkt:
            proto = "UDP"
            info = f"{pkt[UDP].sport} → {pkt[UDP].dport}"
        elif ICMP in pkt:
            proto = "ICMP"
            info = ""
        else:
            proto = "OTHER"
            info = ""

        print(f"{proto:4} | {src:15} → {dst:15} {info}")

print("🚀 Sniffer started (Ctrl+C to stop)")
sniff(iface=ACTIVE_IFACE, prn=process_packet, store=False)
