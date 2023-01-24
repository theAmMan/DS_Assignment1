from django.http import JsonResponse

#Temporary queue implemented for Part A
list_topics = []

def Topics(request):
    # print("Heeyyy thereee")
    if request.method == 'GET':
        # return JsonResponse({'status':'bar'})
        final_resp = {'status':'success'}
        final_resp['number'] = len(list_topics)
        return JsonResponse(final_resp)

    elif request.method == 'POST':
        final_resp = {'status':'message'}
        if request.POST.get('topic_name') == None:
            final_resp['status'] = "failure"
            final_resp['message'] = "No key 'topic_name' found in the POST method"
            return JsonResponse(final_resp)
        else:
            return JsonResponse(final_resp)

def registerConsumer(request):
    final_resp = {'status':'failure'}
    if request.method == 'POST':
        #register the consumer
        return JsonResponse(final_resp)

    final_resp['status'] = 'failure'
    final_resp['message'] = 'GET method not supported for this endpoint'
    return JsonResponse(final_resp)


def registerProducer(request):
    final_resp = {'status':'failure'}
    if request.method == 'POST':
        #register the producer
        return JsonResponse(final_resp)

    final_resp['message'] = 'GET method not supported for this endpoint'
    return JsonResponse(final_resp)

def enqueue(request):
    final_resp = {'status':'failure'}
    if request.method == 'POST':
        #Add the log message to the queue
        return JsonResponse(final_resp)

    final_resp['message'] = 'GET method not supported for this endpoint'
    return JsonResponse(final_resp)

def dequeue(request):
    final_resp = {'status':'failure'}
    if request.method == 'GET':
        #Remove and return the log message from the queue
        return JsonResponse(final_resp)

    final_resp['message'] = 'POST method not supported for this endpoint'
    return JsonResponse(final_resp)

def size(request):
    final_resp = {'status':'failure'}
    if request.method == 'GET':
        #Return the number of log messages in the requested topic for the consumer
        return JsonResponse(final_resp)

    final_resp['message'] = 'POST method not supported for this endpoint'
    return JsonResponse(final_resp)