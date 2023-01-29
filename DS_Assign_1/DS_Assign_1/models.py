from django.db import models 

class Topic(models.Model):
    #model for the topic
    topic_name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Producer(models.Model):
    #Model for the producer
    subscribed_topic = models.ForeignKey(Topic, related_name = 'topic',on_delete = models.CASCADE)
    id = models.PositiveIntegerField(default = 1)

class Consumer(models.Model):
    #Model for the consumer
    id = models.PositiveIntegerField(default = 1)
    subscriptions = models.ManyToManyField(Topic, through = 'ConsumerSubscriptions')
    views = models.ManyToManyField(LogMessage, through = 'ConsumerViews')

class ConsumerSubscriptions(models.Model):
    #To store which consumer is subscribed to which topic
    subscribed_topic = models.ForeignKey(Topic, related_name = 'subscribed_topic',on_delete = models.CASCADE)
    user = models.ForeignKey(Consumer, related_name = 'user', on_delete = models.CASCADE)

class LogMessage(models.Model):
    message = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)

    topic_name = models.ForeignKey(Topic, related_name = 'topic_name', on_delete = models.CASCADE)

    class Meta:
        ordering = ['created']

class ConsumerViews(models.Model):
    #To store which consumer viewed which topic
    viewed_log = models.ForeignKey(LogMessage, related_name = 'viewed_log', on_delete = models.CASCADE)
    user = models.ForeignKey(Consumer, related_name = 'user', on_delete = models.CASCADE)