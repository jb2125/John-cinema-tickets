# To run the code and tests

'TicketService' has been implemented and can be used, but the assumption is that this will be done 
by creating an instance of it, (as main.py implies). The file 'test_ticket_service.py' in the test 
directory contains one Class 'TestTicketService' which extensively tests 'TicketService'. The tests 
can be triggered with: 'test_ticket_service.py'. 'unittest'  is used and every method in 'TicketService' 
has a test method running multiple cases. More information is in that file's comments.

## Code structure

The code has been structured in a modular fashion to improve readability and extendability. The 
Class 'TicketService' has private methods to handle validation checks and calculations. It's very 
clear what each emthod does and where it's called. Any small change can be done by editing a 
single method, so no re-writing large quantities of code. Evrything has been written to be fast 
and efficient, mostly avaoiding loops  and nested logic.

## Comments

The code has many comments to explain what each section is doing. some of the comments 
have a double line space above them and contain a long: '-----------' chain. This signifies a 
section-end, next bit of code will be dealing with something different.
  return
The start of classes have a multi-line string literal containing some information on the Class.

## Considerations

Where appropriate, some information has been made immutable. This includes 
'TicketTypeRequest''s fields and the 'account_id' and 'ticket_type_requests' in 
'TicketService'.
\
There are no checks additional to business rules. One that occurs to me is number if Infants 
to Adults ratio. There's an assumption that the Adults won't run out of lap, (for say, 1 Adullt 
and 19 Infants). There's also a max number for account_id that may be needed


