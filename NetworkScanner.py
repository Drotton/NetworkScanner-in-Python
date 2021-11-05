from scapy.all import ARP, Ether, srp

#ip do alvo - Brodcast da rede - Roteador
target_ip = ""
#Protocolo ARP para identificar o MAC Address do target_ip
arp = ARP(pdst = target_ip)
ether = Ether("ff:ff:ff:ff:ff:ff")
packet = ether/arp

#Envia e recebe pacotes da camada 2 - Lista (pacote_recebido, pacote_enviado)
result = srp(packet, timeout=3)[0]

clients = []
for sent, received in result:
    #A cada resposta, append ip e mac address para a lista 'clients'
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

#Print lista
print("Dispositvos conectados na rede:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))


