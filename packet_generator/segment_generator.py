from data_generator import data_generator
import random

class UDP_Segment(object):
    """docstring for UDP_Segment."""

    def __init__(self, payload):
        # Whatever data that is being transmit, in its binary form
        self.payload = payload

        """There is one issue with the source and destination ports as of right
        now. They sometimes generate small numbers that don't add up to the
        standard UDP header length of 8. I'll set this number statically in
        the calculating function for length, but also create an issue for it in
        the repo"""

        # Random source and destination ports
        # Range starts from 1024 since all numbers preceeding this number
        # are well known ports
        self.source_port = data_generator(str(random.randint(1024,65535)))
        self.dest_port = data_generator(str(random.randint(1024,65535)))
        self.length = None

    def display(self):
        # This method displays the objects attributes
        print("\t\t\tSource port:\n")
        print(self.source_port)
        print("\n")

        print("\t\t\tDestination port:\n")
        print(self.dest_port)
        print("\n")

        print("\t\t\tPayoad: \n")
        print(self.payload)
        print("\n")
 


segment = UDP_Segment(data_generator(input("\nWhat is your message?\n")))

segment.display()
