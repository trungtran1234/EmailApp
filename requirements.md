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

1. Add friend (Tri Nguyen)
- **Summary:** User can add friend to their friend list
- **Actor(s):**
	User
- **Pre-condition:**
	1. The user is logged in to their account on website
	2. The user already enter the user name they want to add into the 
search bar	
- **Trigger:**  
	User click "add friend" button
- **Primary Sequence:**
 1.The system displays the friend's profile information, along with an "Add Friend" button
 2. The user select "Add friend" button
 3. The system sends a friend requets to the selected friend's email address
 4. The system notifies the user that their friend request has been sent.
- **Primary Postconditions:** <can be a list or short description> 
The user's friend list is updated to if the friend accept the request or notifies the user if the friend 
rejects the friend request

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>

  	1. If the entered name or email address is invalid, the system displays an error message and prompts the 
user to enter a valid name or email address.
  	2. If a friend request has already been sent to the selected friend, the system displays a message 
indicating that the request has already been sent.
1.  To-do component(Tri Nguyen)
-**Sumamry:** The user can create a to-do list
- **Actor(s):**
        User
- **Pre-condition:**
        The user is logged in to their account on website
- **Trigger:**
        User click "To-do" button or link
- **Primary Sequence:**
 1. The website open a to-do list that showed all the tasks the user has created, sorted in due date
 2. The user write down all the tasks
 3. The user set the due date
- **Alternative sequencde:**
	If the user does not have any to-do tasks, the system prompts message the user has no tasks.
- **Post Condition:**
	The user is able to mark a task as complete, and delete a task
3. Sort messages based on date
Summary: The user can sort the emails from oldest to newest or newest to oldest
Actors: User
Pre-conditions: The user must be logged in
Trigger: Click the sort button and select by date
Primary Sequence:
User clicks the sort button
Options show up asking what kind of sorting is wanted
User selects the sort by date(oldest to newest)
Alternative Sequence:  There are no emails available to be sorted
Message saying “No message available to sort”
	Post-Condition: The emails are now sorted from oldest to newest or There are no emails that were ever 
sent to the user so a “No  message available to sort” appears.


Name: Search messages
Summary: The use can enter keywords to look for a specific email that contains these keywords
Actors: User
Pre-conditions: The user must be logged in
Trigger: Selecting the search bar and type in specific keywords of what you are searching for
Primary Sequence:  
User selects the search bar
User types in key words that may be contained in the title, sender, subject, or body of the message
A list of received messages with a match appear
User selects the message they are looking for
Alternative Sequence: User entered key words that yielded no results
Message saying “Not found” shows up
	Post-Condition: Messages that have matching keywords from the search bar are displayed OR “Not Found” 
message is displayed as there are no matches


