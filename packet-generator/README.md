# The Packet Generator

The packet generator feature will start with the data class. The following diagram shows what is expected out of the code creating the data.

```mermaid
---
title: Data example
---
classDiagram
    Data : +int binary
    Data : +String text_data
    Data: +data_generator()
    Data: +serialize(text_data)
```
This data class will be the parent class to the network packet. The packet will be built in a series of stages, starting with the UDP packet as shown below.
```mermaid
packet
title UDP Packet
+16: "Source Port"
+16: "Destination Port"
32-47: "Length"
48-63: "Checksum"
64-95: "Data (variable length)"
```
The attributes and methods within the class will be as follows.
```mermaid
---
title: UDP example
---
classDiagram
    UDP : +int source_port
    UDP : +int dest_port
    UDP : +int length
    UDP : +int checksum
    UDP : +int data
    UDP : +packet_creation(source_port, dest_port, length, checksum, data)
    UDP: +packet_verification(self)
```
We will begin with the UDP packet because it is a simpler network packet than the TCP packet, which has many other headers (and therefore data) included in the packet. You can see this in the TCP packet below.

```mermaid
---
title: "TCP Packet"
---
packet
0-15: "Source Port"
16-31: "Destination Port"
32-63: "Sequence Number"
64-95: "Acknowledgment Number"
96-99: "Data Offset"
100-105: "Reserved"
106: "URG"
107: "ACK"
108: "PSH"
109: "RST"
110: "SYN"
111: "FIN"
112-127: "Window"
128-143: "Checksum"
144-159: "Urgent Pointer"
160-191: "(Options and Padding)"
192-255: "Data (variable length)"
```
This will be the first task in the project.

### Directions
1. Accept the task in Github projects in this repository
2. Build the data class, then its relevant child classes (the UDP packet, and the TCP packet).
3. Submit the pull request and I will review it.

If you have any questions let me know. I will be dropping some information in the docs folder and the discord to help you with your research on how to do this.
