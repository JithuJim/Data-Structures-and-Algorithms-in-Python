import datetime, threading
from threading import Thread
import time

class Alice:

	def __init__(self):
		self.packet_box = []

	def create_packet(self):
		packet_string = "Packet "				
		self.packet_box.append(packet_string)		

	def send_packet(self):		
		return self.packet_box.pop(0)

	

class Bob:
	def __init__(self):
		self.received_packets = []

	def receive_packets(self):
		t = threading.Timer(1, self.receive_packets)
		t.start()
		a = Alice()
		a.create_packet()
		self.received_packets.append(a.send_packet())
		if len(self.received_packets) == 6:
			t.cancel()

	def read_packets(self):
		t = threading.Timer(1, self.read_packets)
		t.start()
		if self.received_packets:
			self.received_packets.pop(0)
		else:
			t.cancel()
		print self.received_packets	

def execute():
	b=Bob()
	b.receive_packets()
	time.sleep(15)
	b.read_packets()


execute()		



				


							
				


