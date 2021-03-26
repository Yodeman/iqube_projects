### **LINUX OS AND LINUX COMMANDS**

I will not be able to install Linux OS on my laptop due to the kind of laptop I am using and I as well have space issue (my hard disk drive is almost full, i.e I won’t be able to partition it), but I am quite familiar with Linux environment on virtual machines from platform like Microsoft azure and google cloud platform. For this task, I practiced the Linux command using Cygwin and Git Bash command line interface.

 

Some of the commands I learnt are:

1.   man <command> command which is used to check the documentation of what a command does. <command> --help does similar thing.

2.   touch command can be used to create files.

3.   ls command which is used to list the contents of a directory.

4.   mkdir command which is used to create a new directory.

5.   rmdir command which can be used to delete a directory.

6.   gzip command which is used to compress files.

7.   cat command which is used to view the content of a file. It can be used to concatenate files into another single file.

8.   nano command which is used to open a file for editing.

9.   gunzip command is like gzip command but default to decompressing .gz files.

10. cd command which is used to change directory.

11. find command which is used to search for files for folders.

12. tar command which is used to group multiple files into a folder thereby creating a .tar file containing all the grouped files.

13. grep command which is used to search to tokens in a file.

14. sort command which can be used to arrange content of a file. It can as well be used to arrange the output of other commands.

15. wc command which shows a little concise imformation about a file. It shows the number of words in the file, the number of lines and the size of the file.

16. cp command which is used to to copy files to another location. Files in a directory can be copied recursively as well.

17. mv command which is used to move a file/folder from one directory to another directory.

18. diff command which when executed shows the difference between files. Directories can as well be compared for differences using this command.

19. du command which is used to calculate the size of directory.

20. df command which is used to show the disk usage.

21. ps command which is used to list the processes running in the current user session.

22. kill command, although its main purpose is to terminate processes but it can as well be used for other things .e.g kill --CONT PID which is used to continue as stopped process.

23. which command which provides the path to an excutable.

24. nohup command is used to tell to process to not stop even if there is an issue with network connection between say my computer or a virtual machine.

I was unable to practice commands like sudo, top e.t.c due to the application I am using but I quite understand what they are used for.

![linux_command1](https://github.com/Yodeman/iqube_projects/blob/main/review_learn/linux_command1.png)![linux_command2](https://github.com/Yodeman/iqube_projects/blob/main/review_learn/linux_command2.png)![linux_command3](https://github.com/Yodeman/iqube_projects/blob/main/review_learn/linux_command3.png)![linux_command4](https://github.com/Yodeman/iqube_projects/blob/main/review_learn/linux_command4.png)







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
