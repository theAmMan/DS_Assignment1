# DS_Assignment1
- To first run the server, go to the folder with manage.py and run the command: "python manage.py runserver"
- To do a curl GET request at the endpoint consumer/consume, do this: 'curl "http://127.0.0.1:8000/consumer/consume?topic_name=testing&consumer_id=6"'(params after the ?)
- To do a curl POST request at the endpoint producer/produce, do this: '>curl -X POST http://127.0.0.1:8000/producer/produce -d "topic_name=testing&producer_id=4&message=yo1234567"'(you have to do the curl requests from another terminal)
- The database may already have some topics, consumers and producers currently, we will reset all that when we switch to postgresql