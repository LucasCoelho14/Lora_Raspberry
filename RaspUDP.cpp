#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <wiringPiSPI.h>
#include <wiringPiSerial.h>

#define UDP_PORT 1234

int main() {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "Failed to initialize WiringPi\n");
        return 1;
    }

    int udpSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (udpSocket == -1) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in serverAddr, clientAddr;
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(UDP_PORT);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    if (bind(udpSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("bind");
        return 1;
    }

    printf("UDP listener started on port %d\n", UDP_PORT);

    while (1) {
        char buffer[256];
        socklen_t clientAddrLen = sizeof(clientAddr);
        int bytesRead = recvfrom(udpSocket, buffer, sizeof(buffer) - 1, 0, (struct sockaddr *)&clientAddr, &clientAddrLen);
        if (bytesRead == -1) {
            perror("recvfrom");
            continue;
        }

        buffer[bytesRead] = '\0';
        printf("Received from %s: %s\n", inet_ntoa(clientAddr.sin_addr), buffer);
    }

    close(udpSocket);
    return 0;
}
