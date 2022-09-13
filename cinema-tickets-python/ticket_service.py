
from ssl import SSL_ERROR_WANT_X509_LOOKUP
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService

class TicketService:

  """
  Assumptions:
  - This Class will not be used statically, instances will be made. (the
  code in main implies this is the case).
  - '__ticket_type_requests' is a list of TicketTypeRequest instances, all
  made under the same __account_id

  Notes on this code:
  - To be robust, this code will accept non int account_id (and convert
  them, to int) as there's no indication they defineltty won't occur.
  - The class 'TicketTypeRequest' has been made immutable, (read comment
  there). For this class ('TicketService'), account_id and the ticket
  type request are being made immutable. This avoids chance of them
  getting mistanly changed by other code prior to payment and reservation.
  """

  def __init__(self):
     pass

  def purchase_tickets(self, __account_id=None, __ticket_type_requests=[]):
    
    # Assuming '__ticket_type_requests' is a list of TicketTypeRequest
    # instances, (made from the same account/__account_id)

    # First check that neither account ID nor requests are null entries
    if __account_id == None or __ticket_type_requests == []:
      print("Either account_id and/or order details is missing")
      raise InvalidPurchaseException

    # Run validation method on __account_id
    __account_id = self.__validate_id(__account_id)

    # Run methd to check ticket_type_requests is of corect types
    self.__validate_requests(__ticket_type_requests)

    # Run method to check order has at least one Adult ticket
    self.__validate_one_adult(__ticket_type_requests)

    # Validate number of seats, if valid, save the number
    self.total_seats = self.__validate_order_size(__account_id,
      __ticket_type_requests)


    #--------------------------------------------------------
    # Validation complete, geting cost and making calls to
    # 'SeatReservationService' and 'TicketPaymentService'

    # Run method to get cost of the order
    self.total_cost = self.__calculate_cost(__ticket_type_requests)
    
    # Make calls to payment and seat reservation services
    seat_booker = SeatReservationService()
    pay_service = TicketPaymentService()
    seat_booker.reserve_seat(__account_id, self.total_seats)
    pay_service.make_payment(__account_id, self.total_cost)

  
  # ---------------------------------------------------------------
  # All auxillary (mostly validation) methods are below, (private, as these
  # methods have been developed solely for this class):
 
  # Method to check account ID is valid, (check it's a non-trivial posiyive int, or
  # equivalent string or float.) Avoiding logic nesting in interest of speed
  def __validate_id(self, account_id):
    invalid_id = type(account_id) == str and not account_id.isnumeric()
    invalid_id |= type(account_id) == float and account_id != int(account_id)
    invalid_id |= type(account_id) in [int, float] and account_id < 1
    invalid_id |= type(account_id) not in [int, float, str]
    if invalid_id:
      raise InvalidPurchaseException("__account_id must be an integer > 0")
    else: account_id = int(account_id)
    return account_id    # ensuring account_id is an int after call

  # Check '__ticket_type_requests' contains only objects of Class:
  # 'TicketTypeRequest'
  def __validate_requests(self, ticket_type_requests):
    requests_number = len(ticket_type_requests)
    types_correct = sum([type(el) == TicketTypeRequest for el in
      ticket_type_requests]) == requests_number
    if not types_correct:
      raise TypeError("All elements of __ticket_type_requests must be \
        instances of the correct Class (TicketTypeRequest)")

  # Check order size is > 0 and < 21, if valid, return total seats.
  def __validate_order_size(self, account_id, ticket_type_requests):
    total_seats = sum([el.get_tickets_number() for el in 
      ticket_type_requests if el.get_ticket_type() != "INFANT"])
    total_people = sum([el.get_tickets_number() for el in 
      ticket_type_requests])
    if total_people > 20:
        print("Tickets in single order from accound ID: " + 
          str(account_id) + ", exceeds max of 20")
        raise InvalidPurchaseException
    elif total_people < 1:
        print("There are zero people in this order")
        raise InvalidPurchaseException
    return total_seats

  # Validate that at least one adult is included in the order
  def __validate_one_adult(self, ticket_type_requests):
    # Assuming ADULT ticket requets could occur any number of times,
    # (including 0).
    adult_tickets = sum([el.get_tickets_number() for el in 
      ticket_type_requests if el.get_ticket_type() == "ADULT"])
    if adult_tickets == 0:
        print("Order must have at least 1 Adult ticket")
        raise InvalidPurchaseException

  # this method loops through the requests and calculates price
  def __calculate_cost(self, ticket_type_requests):
    total_cost = 0
    for request in ticket_type_requests:
        if request.get_ticket_type() == "ADULT":
            total_cost += request.get_tickets_number() * 20
        elif request.get_ticket_type() == "CHILD":
            total_cost += request.get_tickets_number() * 10
    return total_cost

  

    