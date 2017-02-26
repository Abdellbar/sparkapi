#!/usr/bin/python
import unirest
import simplejson as json
 

class messages:
    def __init__( self, id='0',roomId='0',text='0',personId='0'):
      self.id       = id
      self.roomId   = roomId
      self.text     = text
      self.personId = personId

class rooms:
    def __init__( self, id='0'):
      self.id       = id
      self.title    = title


class sparkapi(messages,rooms):

  def __init__( self, key='0'):
      self.key = key

  def load_key(self,keyfiel):
    self.key = 'Bearer '+(json.loads(open(keyfiel).read()))['spark_key']
    return self.key


  def get_msg(self,id):
    response_message = messages(id)
    #print "ID:"+id
    #print self.key
    response = unirest.get("https://api.ciscospark.com/v1/messages/"+id,
      headers={
        "Authorization": self.key
      }
    )
    #print response
    #print response_message.id
    response_message.id       = response.body['id']
    response_message.roomId   = response.body['roomId']
    response_message.text     = response.body['text']
    response_message.personId = response.body['personId']

    #print response_message
    #cmnd_list = cmnd_text[1].split('|')
    #print string
    return response_message

  def post_msg(self,roomId,text):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": self.key,
        "Content-Type":"application/json"
      },
      params=json.dumps({"roomId":roomId,"text":text})
    )
    print response.body

  def list_rooms(sef):
    roomlist = []
    room     = rooms()
    response = unirest.get("https://api.ciscospark.com/v1/rooms",
      headers={
        "Authorization": self.key,
        "Content-Type" : "application/json"
      }
    )
    #print response
    #print response_message.id
    for item in response.body['items']:
      room.id   = item['id']
      room.text = item['title']
      roomlist.append(room)

    return roomlist  
