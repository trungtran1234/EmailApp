## Functional Requirements

User should be able to:
1. Move messages to trash - Trung
2. Recover trashed messages - Trung
3. Delete trashed messages permanently - Jasper
4. Bookmarking/archive messages - Kevin
5. Compose messages - Kevin
6. Create an account - Trung
7. View incoming messages - Jasper
8. View sent messages - Kevin
9. Remove Friend - Tri Nguyen
10. Create to-do list -  Tri Nguyen
11.Search messages - Jasper
12. Add Friend - Tri Nguyen


## Non-functional Requirements

1. Messages should have font Arial in size 12
2. Compatible with Google Chrome, Safari, Microsoft Edge, Opera, and Firefox


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
	
Name: Delete messages inside of trash permanently
Summary: The use can go into the trash section and choose to permanently delete an email 
Actors: Users
Pre-conditions: The user must be on the trash section
Trigger: selecting delete permanently on the email
Primary Sequence:  
1.Right click on the email that is getting deleted
2.Click the delete button
3.Press the confirm button
Alternative Sequence: There are no emails in the trash
Post-Condition: The email is now gone after being successfully deleted
OR
There was no email in the trash to begin with



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


Name: Bookmarking messages
Summary: The user can click on an icon to bookmark messages in their inbox 
Actors: User that is bookmarking the message
Pre-conditions: User must be logged in, and have a message in their inbox 
Trigger: Clicking on the bookmark icon
Primary Sequence:
2. User goes into their inbox
3. User clicks the bookmark icon on the message they want to bookmark
4. Message will appear on their bookmark folder
Alternative Sequence:
1. User clicks the bookmark icon on a message that is already bookmarked, then message is removed from the bookmark folder 
Post-Conditions:
1. Message appears in the bookmark folder, and the message will be marked
OR
2. Message will disappear from the folder when a user clicks on an already bookmarked message

Name: Composing messages
Summary: The user clicks on the "compose" button to create an email draft where they will enter text or files onto the textbox, and pick a recipient to send to 
Actors: User creating the email
Pre-conditions: User must be logged in, and in the inbox page
Trigger: User clicks on the "compose" button
Primary Sequence:
1. User enters message in draft
2. User types subject in subject line
3. User enters the name or email address of user they want to send to.
4. User clicks "Send"
Alternative Sequence:
1. If user clicks "Send" without entering a recipient, then message prompts user to enter a recipient
2. If user clicks "Send" without sending a subject, then it will send a message with an empty subject line
3. If user clicks "Send" without entering a message in the draft, then an empty message will be sent to the recipient
Post-Conditions:
1. Message will appear in the recipient's inbox
2. Message will appear in sent messages folder
	
Name: Register an account
Summary: A user on the website can register for an account to use its application
Actors: The user registering for the website
Pre-conditions: The user must be on the website and not already logged in
Trigger: Click the “Create account” button
Primary Sequence: 
1. The user fills out the email, password, and username on the registration form
2. The user click “Register” to send in the registration
3. The system makes the account and automatically log the user in with their new account
Alternative Sequence:
1. If the email already has an account, the system outputs an error message that prompts the user to enter a valid email address.
2. If the username is taken, the system outputs an error message that prompts the user to try a different username.
3. If either the email, username, or password is left empty, the system outputs an error message that prompts the user to fill out all the fields.
Post Condition: The user made the new account and can log in, or the user fails to make the new account and can’t log in.
	
Name: Remove friend
Summary: A user on the website can remove a friend that they have added
Actors: The user trying to remove a friend
Pre-conditions: The user must be on the website and logged in
Trigger: Click the “Friends” button to go to their friends tab
Primary Sequence:
1. The user selects the friend they want to remove by clicking on their profile
2. The user clicks “Remove Friend” button displayed on the screen
3. The system displays “Confirm” and “Cancel” button on the screen
4. The user clicks “Confirm” button displayed on the screen to remove the friend
Alternate Sequence:
1. The user selects “Cancel” instead of “Confirm”, then the prompted buttons disappear and the friend is not removed yet.
2. The user have no friend in their friends list so the user is unable to remove any friend.
Post Condition: The user removed the friend and that friend is no longer in their friend list, or the user cancelled the removal and the friend is still in their friend list.

