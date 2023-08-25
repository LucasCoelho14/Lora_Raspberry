#include <iostream>
#include <cstring>
#include <wiringPi.h>
#include <arpa/inet.h>
#include <sys/socket.h>

const int udpPort = 1234;

int udpSocket;

int main() {
    std::cout << "Initializing WiringPi..." << std::endl;
    wiringPiSetup();

    std::cout << "Creating UDP socket..." << std::endl;
    udpSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (udpSocket == -1) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in serverAddr;
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(udpPort);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    if (bind(udpSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("bind");
        return 1;
    }

    std::cout << "UDP listener started on port " << udpPort << std::endl;

    while (1) {
        char buffer[256];
        struct sockaddr_in clientAddr;
        socklen_t clientAddrLen = sizeof(clientAddr);

        int bytesRead = recvfrom(udpSocket, buffer, sizeof(buffer) - 1, 0, (struct sockaddr *)&clientAddr, &clientAddrLen);
        if (bytesRead == -1) {
            perror("recvfrom");
        } else {
            buffer[bytesRead] = '\0';
            std::cout << "Received from " << inet_ntoa(clientAddr.sin_addr) << ": " << buffer << std::endl;
        }

        // Add your logic and delays here as needed.
    }

    return 0;
}
