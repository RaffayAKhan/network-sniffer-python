from scapy.all import sniff

def test(pkt):
    print("📦 Packet captured!")
    return True

interfaces = [
    r"\Device\NPF_{FFAD5B6A-FA54-42A3-99B1-95E6CCBC9ED3}",
    r"\Device\NPF_{69515B15-A322-40BC-B476-C74ACFD8B3C3}",
    r"\Device\NPF_{CB09AA49-B483-4EEF-BB7B-48FF2C2DA2CB}",
    r"\Device\NPF_{EAB06D23-2F23-44FB-9E58-A623B31F8BAA}",
    r"\Device\NPF_{142FA21E-8FC0-43B2-9530-2A6941B5BB93}",
    r"\Device\NPF_{ADEFD067-F177-4D0F-9494-B23AF4E8E849}",
    r"\Device\NPF_{6D794731-7009-442B-B823-A7951A292340}",
    r"\Device\NPF_{0C1E0EA8-E8BF-43CC-986C-6719069A366B}",
]

for iface in interfaces:
    print(f"\n🔍 Testing {iface}")
    sniff(iface=iface, prn=test, count=3, timeout=5)
