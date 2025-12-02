# The Packet Generator

The Packet Generator section of the code will take binary data and create network segments for transfer over a network. 

The first class will be the UDP class, with the TCP class inheriting from that class since they have some of the same fields.

(Originally the data class was going to be the initial class but there are many different types of data that could potentially be transmit. So although we are initially working with text, to future proof the code we are making the packet segments logic separate from identifying any type of data since network segments don't care anyways. Its the job of the protocol to handle that sort of thing, which gets a little bit into the other layers of the OSI model which I'll go over in another file.)


### The Network Packets
This data class will be the parent class to the network packet. The actual network packets will be built in a series of stages, starting with the UDP packet as shown below.
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

One thing to note is this diagram shows the data types as integers but the payload and the rest of the fields will actually be bytes not just integers but we can refer to them as integers, which I'll explain in another file.
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
