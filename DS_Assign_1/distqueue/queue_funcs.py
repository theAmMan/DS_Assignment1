from .models import *

#basic functions to add the various logs etc in the table
def createTopic(name):
    #create a topic with the given name
    ret_dict = {}
    if name == '':
        ret_dict['status'] = "failure"
        ret_dict["message"] = "Error: Topic name cannot be blank"
        return ret_dict
    topics = Topic.objects.filter(topic_name = name)
    if not topics:
        #query set is empty, the name does not exist
        Topic.objects.create(topic_name = name)
        ret_dict['status'] = "sucess"
        ret_dict["message"] = "Topic "+name+" succesfully created"
        return ret_dict 
    else:
        ret_dict['status'] = "failure"
        ret_dict["message"] = "Error: Topic "+name+" creation failed(It already exists)"
        return ret_dict

def listTopics():
    ret_dict = {'status':'failure'}
    topics = Topic.objects.all()
    if not topics:
        ret_dict["message"] = "Error: No topics are present"
    else:
        ret_dict['topics'] = []
        for x in topics:
            ret_dict['topics'].append(x.topic_name)
            # print(x.topic_name)
        ret_dict['status'] = "success"
    return ret_dict

def qregisterConsumer(topic):
    ret_dict = {'status':'failure'}
    topics = Topic.objects.filter(topic_name = topic)
    if not topics:
        ret_dict['message'] = "Error: Topic does not exist"
    else:
        Consumer.objects.create(cid = Consumer.objects.all().count()+1)

        #retrieve the last object created and add the topic they are subscribed to
        consum = Consumer.objects.filter(cid = Consumer.objects.all().count())[0]
        consum.subscriptions.add(topics[0])
        consum.save()

        ret_dict['status'] = "success"
        ret_dict["consumer_id"] = Consumer.objects.all().count()

    return ret_dict

def qregisterProducer(topic):
    ret_dict = {'status':'success'}
    topics = Topic.objects.filter(topic_name = topic)
    if not topics:
        #if topic does not exist, create the topic
        ret_dict = createTopic(topic)
        if ret_dict['status'] == "failure":
            return ret_dict
        else:
            topics = Topic.objects.filter(topic_name = topic)
    else:
        # print(topics[0].topic_name)
        Producer.objects.create(pid = Producer.objects.all().count()+1, subscribed_topic = topics[0])

        ret_dict["producer_id"] = Producer.objects.all().count()

    return ret_dict

def qenqueue(topic, pid, message):
    ret_dict = {'status':'failure'}
    #Check if topic is present
    topics = Topic.objects.filter(topic_name = topic)
    if not topics:
        ret_dict["message"] = "Error: Invalid topic"
    else:
        producers = Producer.objects.filter(pid = pid)
        if not producers:
            ret_dict['message'] = "Error: Invalid Producer"
            return ret_dict

        if producers[0].subscribed_topic != topics[0]:
            ret_dict['message'] = "Error: Producer is not subscribed to the topic mentioned"
            return ret_dict
        
        LogMessage.objects.create(message = message, prod = producers[0], 
                            topic_name = topics[0])
        ret_dict['status'] = 'success'

    return ret_dict

def qsize(topic, cid):
    #Return the size of the queue for this topic and consumer
    ret_dict = {'status':'failure'}
    topics = Topic.objects.filter(topic_name = topic)
    if not topics:
        ret_dict['message'] = "Error: Invalid topic"
        return ret_dict
    
    consumers = Consumer.objects.filter(cid = cid)
    if not consumers:
        ret_dict['message'] = "Error: Invalid Consumer"
        return ret_dict

    is_subscribed = consumers[0].subscriptions.filter(topic_name = topic)
    if not is_subscribed:
        ret_dict['message'] = "Error: Consumer is not subscribed to the topic"
        return ret_dict
    
    count = 0 
    count += LogMessage.objects.filter(topic_name = topics[0]).count()

    count -= consumers[0].views.all().count()

    ret_dict['status'] = "success"
    ret_dict['size'] = count 
    return ret_dict

def qdequeue(topic, cid):
    #dequeue message from the queue
    ret_dict = {'status':'failure'}
    topics = Topic.objects.filter(topic_name = topic)
    if not topics:
        ret_dict["message"] = "Error: Invalid topic"
        return ret_dict

    consumers = Consumer.objects.filter(cid = cid)
    if not consumers:
        ret_dict['message'] = "Error: Invalid Consumer"
        return ret_dict

    is_subscribed = consumers[0].subscriptions.filter(topic_name = topic)
    if not is_subscribed:
        ret_dict['message'] = "Error: Consumer is not subscribed to the topic"
        return ret_dict

    #Get the first message that is not returned to the consumer
    all_messages = LogMessage.objects.filter(topic_name = topics[0])

    viewed_count = consumers[0].views.filter(topic_name = topics[0]).count()
    if viewed_count == all_messages.count():
        print(viewed_count)
        ret_dict['message'] = "No log message in queue for this request"
        return ret_dict

    #Return that message otherwise
    ret_dict['message'] = all_messages[viewed_count].message
    consumers[0].views.add(all_messages[viewed_count])

    ret_dict['status'] = "success"
    return ret_dict