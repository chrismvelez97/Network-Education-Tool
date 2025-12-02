class UDP_Segment(object):
    """UDP data is connectionless and only needs the bare essentials to send data.
       Here you can see that because the segment needs to know where the data is going
       (the dest_port) and where the data came from (the source_port). The segment also
       needs to know the length of the segment so the receiver knows when to stop listening
       for more segments. Checksum is optional but can be included later."""

    def __init__(self, payload):
        """This function is always created when making a class. It is the method that
        creates new instances of the class, otherwise known as instantiation.
        
        Every single time a network segment gets created, these are the things that need
        to be created. self refers to the insantiated object, and payload refers to the
        data that is being turned into a network segment."""
        
        # Whatever data that is being transmit, in its binary form
        self.payload = payload

        # These are statically set ports. Later we will set these dynamically
        self.source_port = bytes([0b00000111, 0b11010000])
        self.dest_port = bytes([0b00000111, 0b11010001])

        # This calculates the size of the UDP segment, offsetting by 8 bytes for the header info.
        self.total_length = 8 + len(payload)

    def display(self):
        """This display function will show what the network segment looks like after some data has been fed into the class instantiation."""
        
        """The backslash followed by either an n or t is just for organizing the visual printout of the code."""
        
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

# This code below is just for testing.
# message = input("\nWhat is your message?\n\n").encode()
#
# segment = UDP_Segment(message)
#
# segment.display()
