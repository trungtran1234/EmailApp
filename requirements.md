## Functional Requirements

1. Restore deleted messages 
2. Delete messages 
3. Bookmarking/archive messages - Kevin
4. Compose messages - Kevin
5. Create an account - Trung
6. View incoming mesesages - Jasper
7. View sent messages 
8. View deleted messages
9. Advance search items with filters - Trung
10. Manage tasks in to-do component -  Tri Nguyen
11. Search messages - Jasper
12. Add Friend - Tri Nguyen

## Non-functional Requirements

1. Multilingual
2. Work on all browsers

## Use Cases

1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...
2. Use Case Name (Should match functional requirement name)
   Name: Sort messages based on date
Summary: The user can sort the emails from oldest to newest or newest to oldest
Actors: The use that is trying to sort their email by date
Pre-conditions: The user must be logged in
Trigger: Click the sort button and select by date
Primary Sequence:
User clicks the sort button
Options show up asking what kind of sorting is wanted
User selects the sort by date(oldest to newest)
Alternative Sequence:  There are no emails available to be sorted
Message saying “No message available to sort”
	Post-Condition: The emails are now sorted from oldest to newest
				OR
			      There are no emails that were ever sent to the user so a “No  message available to sort” appears.


Name: Search messages
Summary: The use can enter keywords to look for a specific email that contains these keywords
Actors: The use that is trying to search for a specific message
Pre-conditions: The user must be logged in
Trigger: Selecting the search bar and type in specific keywords of what you are searching for
Primary Sequence:  
User selects the search bar
User types in key words that may be contained in the title, sender, subject, or body of the message
A list of received messages with a match appear
User selects the message they are looking for
Alternative Sequence: User entered key words that yielded no results
Message saying “Not found” shows up
	Post-Condition: Messages that have matching keywords from the search bar are            displayed
OR
 			“Not Found” message is displayed as there are no matches


