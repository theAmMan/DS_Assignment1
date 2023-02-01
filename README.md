# DS Assignment1 : Implementing a Distributed Queue
Date: Jan 31, 2023

*Contributed By :* 

[Esha Manideep Dinne](https://github.com/idealover)  -     19CS10030  
[Amartya Mandal](https://github.com/theAmMan)           -     19CS10009  
[Divyansh Bhatia](https://github.com/Divyansh221)           -     19CS10027  
[Anish Sofat](https://github.com/anishsofat)                   -     19CS10011  
[Rupinder Goyal](https://github.com/rupinderg00)            -     19CS10050  

# How to Run
## Http CURL requests
- To first run the server, go to the folder with manage.py and run the command: "python manage.py runserver"
- To do a curl GET request at the endpoint consumer/consume, do this: 'curl "http://127.0.0.1:8000/consumer/consume?topic_name=testing&consumer_id=6"'(params after the ?)
- To do a curl POST request at the endpoint producer/produce, do this: '>curl -X POST http://127.0.0.1:8000/producer/produce -d "topic_name=testing&producer_id=4&message=yo1234567"'(you have to do the curl requests from another terminal)
- The database may already have some topics, consumers and producers currently, we will reset all that when we switch to postgresql
 
## Test File
A test file is provided : Testing.py  
Command to run test file : python Testing.py

# Info
A distributed queue is a type of data structure that is designed to hold and manage a large number of items or tasks in a distributed system.  
It allows multiple processes to add and remove elements from the queue simultaneously, and ensures that tasks are processed in a first-in-first-out (FIFO) order across all nodes in the system. This helps to balance the workload and prevent bottlenecks in large-scale systems.

## Part A
We have implemented the distributed logging queue using Python along with Django, which is a high level python framework for supporting REST APIs.  
The Queue for maintaining the log messages is implemented in the file distQueue.py. This file introduces a class distQueue that keeps track of topics, log messages, producers, consumers and provides functionalities to add and view messages (enqueue, dequeue) as well as introduce new users (registerProducer, registerConsumer) and topics (createTopic) and to list present topics (listTopics) and length of queue for them (size).

## Part B
We have added persistence to the distributed queue, so that log messages are stored in a persistent storage layer and can be retrieved even if the server crashes or restarts.  
Database is implemented using PostGRESQL. Django handles all the low level detail communication with the Database. There are multiple models(tables) for Topics, Producers, Consumers, LogMessages. There are two other linking tables which link consumers with their subscriptions (Consumer Subscriptions) and log messages to the consumers who viewed the messages (consumerViews).

## Part C
We created a Python library which acts as an abstraction using which producers and consumers can communicate with our distributed logging queue using a more convenient or efficient interface.  
A package is implemented containing the class myQueue, which provides an easy to use user interface for any user using this distributed logging queue system. The class stores the server link, and provides functions to users to create topics, list topics, register consumers, register producers, enqueue, dequeue and get the size of the queue. These functions take the parameters as inputs and call the necessary requests to the http server.
