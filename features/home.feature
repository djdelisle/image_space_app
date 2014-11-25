Feature: A new user comes to home page, clicks on the Sign-up page to sign up and would be able to do all the functions the website offers


Scenario: New user tries to sign up, go back to the home page then sign in when done then post up picture and log out
Given I am a new user
I load the "home" page
I press Sign-up to go to sign-up page
And I fill in "Username-input" with "user"
And I fill in "Email address-input" with "user@email.com"
And I fill in "Password-input" with "password"
I press "Sign-up"
I click "Home" to go back to the home page
And I fill in "Email address-input" with "user@email.com"
And I fill in "Password-input" with "password"
I press "Login"
I press Upload to get to upload page
I press browse to choose picture
I press submit to upload
I press Home to go back to the home page
I see the all pictures that were posted
I press Logout
I see the header "ImageSpace"