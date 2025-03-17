[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18587633)
# CSSE6400 Week 2 Practical

Integration of a local relational database into our application.

Please see the [instructions](https://csse6400.uqcloud.net/practicals/week02.pdf) for more details.

Update this README file with appropriate information about your project,
including how to run it.

## Database

Created a database for our API to retrieve, update and delete information from. Used SQAlchemy to implement (written in sqlite).
Also created a helper method to convert the model to a dictionary. This allows lookups by a key value (get()).

## Routing

Heavily modified routing to implement each of the GET, POST, PUT, DELETE api functions.

## Testing

Created a class **TodoTest**, which includes a setup func to initialise the testing environemnt database and a function to ensure the response exists within the data it is trying to fetch.

### Routing Updats

Some of the routes had to be modified to conform to the now implemented tesing conditions (e.g. excluding 'completed' items from the returned list of todo items in get_todos()).

There are [resources](https://www.makeareadme.com) available to help you write a good README file.


