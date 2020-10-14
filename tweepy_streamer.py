from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pykafka import KafkaClient
import json

ckey=
csecret=
atoken=
asecret=


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        message = json.loads(data)
        if message['place'] is not None:
            client = get_kafka_client()
            topic = client.topics['twitterdata_new']
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
    stream.filter(track = ['Donald Trump', 'Joe Biden'])