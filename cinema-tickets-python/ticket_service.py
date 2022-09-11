
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest

class TicketService:

  """
  purchase_tickets should be the only public method
  """

  def purchase_tickets(account_id=None, ticket_type_requests=[]):
    
    # Assuming 'ticket_type_requests' is a list of TicketTypeRequest
    # instances, (made from the same account)

    # First check that neither account ID nor requests are null entries
    if account_id == None or ticket_type_requests == []:
      raise InvalidPurchaseException

    # Check account ID is valid, (check if non trivial posiyive int, or
    # equivalent string or float. Avoiding logic nesting

    invalid_id = type(account_id) == str and not account_id.isnumeric()
    invalid_id |= type(account_id) == float and account_id != int(account_id)
    invalid_id |= type(account_id) in [int, float] and account_id < 1
    if invalid_id:
      raise InvalidPurchaseException("account_id must be an integer > 0")
    else: account_id = int(account_id)

    # Check 'ticket_type_requests' contains only the correct objects
    requests_number = len(ticket_type_requests)
    types_correct = sum([type(el) == TicketTypeRequest for el in ticket_type_requests]) == requests_number
    if not types_correct:
      raise TypeError("All elements of ticket_type_requests must be of the correct Class (TicketTypeRequest)")
    
    # Check order size is > 0 and < 21
    if sum([el.get_ticket_number for el in ticket_type_requests]) > 20:






