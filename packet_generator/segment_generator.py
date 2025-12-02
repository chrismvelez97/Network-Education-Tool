class UDP_Segment(object):
    """docstring for UDP_Segment."""

    def __init__(self, payload):
        # Whatever data that is being transmit, in its binary form
        self.payload = payload

        self.source_port = bytes([0b00000111, 0b11010000])
        self.dest_port = bytes([0b00000111, 0b11010001])
        self.total_length = 8 + len(payload)

    def display(self):
        # This method displays the objects attributes
        print("\n\t\t\tSource port:\n")
        print("\t\t\t" + str(self.source_port))
        print("\n\n")

        print("\t\t\tDestination port:\n")
        print("\t\t\t" + str(self.dest_port))
        print("\n\n")

        print("\t\t\tLength:\n")
        print("\t\t\t" + str(self.total_length))
        print("\n\n")

        print("\t\t\tChecksum: \n")
        print("\t\t\t0")
        print("\n")

        print("\t\t\tPayload: \n")
        print("\t\t\t" + str(self.payload))
        print("\n")

# message = input("\nWhat is your message?\n\n").encode()
#
# segment = UDP_Segment(message)
#
# segment.display()
