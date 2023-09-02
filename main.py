import socket

discord="dao026"#bana burdan ulaşabilirsiniz
hedef_ip = input("Hedef İp: ")
baslangic_port = 1
son_port = 1024 

# Belirtilen port aralığını tara
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET ipv4 SOCK_STREAM tcp port
    sock.settimeout(1)  # Her port için bir saniye zaman aşımı belirleyin

    # Portu dene
    result = sock.connect_ex((target_ip, port))#connect_ex 0 yada 1 değer döndürür 0 başarılı bağlantı 1 başarısız bağlantı

    if result == 0:
        print(f"Port {port}: Açık")


    sock.close()
