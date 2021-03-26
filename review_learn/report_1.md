### **Domain Name System (DNS)**

This is a service that runs on all computers or generally the internet service at large. The system works by resolving website URL to an IP address. So, if a device tries accessing a website, the DNS service on the device contacts the IP server (residing somewhere in the world) to get information on the IP server, if the IP server has information about the IP address it returns it to the device DNS else, the IP server contacts the name services (.e.g. ‘.com’ name service) to get information on the targeted IP address. Once the name services gets the IP address, it relays the information back to the IP server which then relays it back to the device DNS. The IP server cache the returned information on the targeted IP address in order to have fast response he next time a query about such service is requested.

 

### **Open System Interconnection (OSI) Model**

This is basically concerned with how data are transferred over the network. It consists of layers which are package protocols:

​     **Application Layer**: This layer is made up of protocols like file transfer protocol (FTP) which is used for file transfer, Hypertext transfer protocol which is used for web surfing, SMTP for emails etc. These protocols are used by network applications i.e. computer applications that can connect to internet to communicate with internet. 

​     **Presentation Layer**: This layer receives data from the application layer inform of characters and numbers. This layer then converts the received data into machine code. It compresses and encrypt (on the sender side) the data received in order to enable fast and secure transfer of data.

​     **Session Layer**: This layer helps in setting up and managing connections .i.e. sending and receiving of data and termination of connections/sessions. It does this through application programming interfaces.

​     **Transport Layer**: This layer controls the reliability of communication through segmentation, flow control and error control. The segmentation helps to break data into chunks and send to target applications. Flow control helps to manage the rate at which data are sent and received. The error control helps to ensure that the data sent is same as the one received.

​     **Network Layer**: This layer is concerned with transmission of received data from a device to another device connected over the network.

​     **Data Link Layer**: This layer provides access to data for higher levels of OSI model layer. It also controls how the data are accessed.

​     **Physical Layer**: It converts the binary data from the data link layer into sequence depending on the media used (wireless, cable).

 

**GRAPH THEORY**

A mathematical aspect model that deals with the study of graphs. A Graph is a collection of vertices (nodes) and edges. Graph theory is concerned with connections among vertices (nodes in computing term) and it has proved to be very useful in computing as it helps to model problem and helps to solve them efficiently (.e.g. graph theory helps to model how information are relayed fast in networking as each device accessing the internet can be modeled as vertices and the route the data follows as edges).