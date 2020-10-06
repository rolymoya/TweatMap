from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pykafka import KafkaClient
import json

ckey="EKpIrdJybEDinsTpRCVIHnMuk"
csecret="8isBN5Nn0eFGoqP98SN6PT6MFzprnZ1L4JRUA5KAVI6BfFdmDB"
atoken="1309643487852269568-GC8O7WuNLlU6G2BJnKUe3fgXk4CPgC"
asecret="B9huP5TCLAvxf4rXIEKGL16MOKIGJN5Kd7ymaT4Ljz3j0"


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        message = json.loads(data)
        if message['place'] is not None:
            client = get_kafka_client()
            topic = client.topics['twitterdata']
            producer = topic.get_sync_producer()
            producer.produce(data.encode('ascii'))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    listener = StdOutListener()
    stream = Stream(auth, listener)
    stream.filter(track = ['Donald Trump'])