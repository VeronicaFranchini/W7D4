import socket 
import random
import string



def getPacket():
    packet = ""
    while len(packet) < 1024 + 1 :
        packet += random.choice(string.hexdigits)
    return packet
def main():
    target_ip = input("Inserisci indirizzo ip: ")
    udpport = int(input("Inserisci numero porta: "))
    num_packet = input("Inserisci numero di pacchetti: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((target_ip, udpport))
    for x in range(0, num_packet, 1):
        s.sendall(getPacket().encode('utf-8'))
    print(f'{x}pacchetti inviati' )
    s.close()

if __name__ -- '__main__' :
    main()