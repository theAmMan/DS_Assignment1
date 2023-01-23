class distQueue:
  def __init__(self):
    self.reg_prod = {}
    self.reg_cons = {}
    self.topics = []
    self.queue = {}
    self.cid = 1
    self.pid = 1
  def createTopic(self,name):
    if name in self.topics:
      return "Topic "+name+" creation failed"
    self.topics.append(name)
    self.queue[name] = []
    return "Topic "+name+" succesfully created"
  def listTopics(self):
    if self.topics:
      return self.topics
    return "No topics are present"
  def registerConsumer(self,topic):
    if topic in self.topics:
      if topic in self.reg_cons.keys():
        self.reg_cons[topic].append(self.cid)
      else:
        self.reg_cons[topic]=[self.cid]
      self.cid+=1
      return self.cid-1
    return "Topic does not exist"
  def registerProducer(self,topic):
    if topic in self.topics:
      if topic in self.reg_prod.keys():
        self.reg_prod[topic].append(self.pid)
      else:
        self.reg_prod[topic]=[self.pid]
      self.pid+=1
      return self.pid-1
    return "Topic does not exist"
  def enqueue(self,topic, pid, message):
    if topic not in self.topics:
      return "Invalid topic"
    if pid not in self.reg_prod[topic]:
      return "Invalid producer"
    self.queue[topic].append((pid,message,[]))
  def dequeue(self,topic,cid):
    if topic not in self.topics:
      return "Invalid topic"
    if cid not in self.reg_cons[topic]:
      return "Invalid consumer"
    n = len(self.queue[topic])
    message = ''
    for i in range(0,n,1):
      if cid not in self.queue[topic][i][2]:
        self.queue[topic][i][2].append(cid)
        self.queue[topic][i][2].sort()
        message = self.queue[topic][i][1]
        if(self.queue[topic][i][2]==self.reg_cons[topic]):
          self.queue[topic].pop(i)
        break
    if message == '':
      return "No log message in queue for this request"
    return message
  def size(self,topic,cid):
    if topic not in self.topics:
      return "Invalid topic"
    if cid not in self.reg_cons[topic]:
      return "Invalid consumer"
    count = 0
    for i in self.queue[topic]:
      if cid not in i[2]:
        count+=1
    return count