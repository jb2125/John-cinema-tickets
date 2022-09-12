import unittest
from ..ticket_type_request import TicketTypeRequest
from ..ticket_service import TicketService

# Testing all aspects of 'TicketTypeRequest'. This requires the
# 'TicketRequest' class, but that's not explicitly tested here.

# Creating ticket requests of varying validity. Naming covention here
# will be simply to save space, but still part descriptive.

# firstly, instance of 1 or both nulls, ()
null_1 = [TicketTypeRequest(None, None)]
null_2 = [TicketTypeRequest("ADULT", None)]
null_3 = [TicketTypeRequest(None, 2)]
# Ticket type requests checks for non: 'ADULT', 'CHILD', 'INFANT' and
# wrong data types

# Number of seats out of range
seats_low = [TicketTypeRequest('ADULT', 0)]
seats_high = [TicketTypeRequest('ADULT', 21)]
seats_high = [TicketTypeRequest('ADULT', 10), TicketTypeRequest(
    'CHILD', 11), TicketTypeRequest('INFANT', 7)]

# Orders with Children and/or Infants, but no Adults
no_adults_1 = seats_low = [TicketTypeRequest('CHILD', 2),
    TicketTypeRequest('ADULT', 0)]
no_adults_2 = seats_low = [TicketTypeRequest('CHILD', 3)]
no_adults_3 = seats_low = [TicketTypeRequest('CHILD', 2),
    TicketTypeRequest('INFANT', 1)]

# Building some valid request lists and their correct cost and seats
valid_1 = [TicketTypeRequest("ADULT", 2), TicketTypeRequest("CHILD", 3),
    TicketTypeRequest("INFANT", 2)]
valid_1_cost = 70
valid_1_seats = 5

valid_2 = [TicketTypeRequest("ADULT", 1)]
valid_2_cost = 20
valid_2_seats = 1

valid_3 = [TicketTypeRequest("ADULT", 10), TicketTypeRequest("CHILD", 10)]
valid_3_cost = 300
valid_3_seats = 20

# Creating orders that are Valid and should work, but verbose
verbose_1 = [TicketTypeRequest('ADULT', 2), TicketTypeRequest("CHILD", 1),
    TicketTypeRequest("ADULT", 1), TicketTypeRequest("CHILD", 2)]


# ------------------- Starting the test class

class Test_Ticket_Servic(unittest.TestCase):

    # First create a 'TicketService' object to test on
    ticket_service = TicketService()



