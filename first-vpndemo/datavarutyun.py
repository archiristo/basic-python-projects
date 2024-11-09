import socket
import threading

# sunucu konfigürasyonu (proxy)

proxy_host = '127.0.0.1'
proxy_port = 8888

# sunucu konfigürasyonu (karşı taraf)

destination_host = 'google.com'
destination_port = '80'

def handle_client(client_socket):
    
    # karşı sunucuya bağlanma aşaması için
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((destination_host, destination_port))

    # veri iletimi
    while True:
        # veri çekiş
        client_data = client_socket.recv(4096)
        if len(client_data) == 0:
            break

        #veri aktarış (assala nasri-aktar)
        server_socket.send(client_data)

    # bağlantı koparma
    client_socket.close()
    server_socket.close()

def start_proxy():
    # soket oluşturma
    proxy = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    # host port socket birleşimi
    proxy.bind((proxy_host, proxy_port))
    # bağlantı bekleme
    proxy.listen(5)

    print(f"Bağlantı bekleniyor {proxy_host}: {proxy_port}")

    while True:
        client_socket, addr = proxy.accept()
        print(f"Connected {addr[0]}: {addr[1]}")

        client_handle = threading.Thread(target=handle_client , args=(client_socket))
        client_handle.start()

if __name__ == "__main__":
    start_proxy()