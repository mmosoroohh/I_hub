# I_hub
Innovation Hub is a platform for data mapping.
This Django API was designed to help focus on areas where personal data is processed.

##Getting started

### Prerequisites

In order to install and run this project locally, you would need to have the following installed on you local machine.

- **Python 3+**
- **Django 2+**
- **Postgresql**

### Installation
* Clone this repository

* Navigate to the project directory `cd I_Hub/`

* Create a virtual environment

* Install dependencies `pip3 install -r requirements.txt`
* Edit `I_Hub/configuration/settings.py` database credentials to your database instance

* Create a Postgresql database 

* Run the command `python3 manage.py makemigrations` 

* Run the command `python3 manage.py migrate` to create and sync the postgresql database (you must have the database previously created with name 'hub_db').

* Run the command `python3 manage.py runserver`

* Run development server


## Testing API endpoints
<table>
<tr><th>Test</th>
<th>API-endpoint</th>
<th>HTTP-Verbs</th>
</tr>
<tr>
<td>Register a user</td>
<td>/api/users/register</td>
<td>POST</td>
</tr>
<tr>
<td>Login a user</td>
<td>/api/users/login</td>
<td>POST</td>
</tr>
<tr>
<td>Create an asset</td>
<td>/api/assets</td>
<td>POST</td>
</tr>
<tr>
<td>Get an asset</td>
<td>/api/assets/id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit an asset</td>
<td>/api/assets/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete an asset</td>
<td>/api/assets/id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a process</td>
<td>/api/process/id</td>
<td>POST</td>
</tr>
<tr>
<td>Fetch a process</td>
<td>/api/process/id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit</td>
<td>/api/process/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a process</td>
<td>/api/process/id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a group</td>
<td>/api/groups</td>
<td>POST</td>
</tr>
<tr>
<td>Get a group</td>
<td>/api/groups/id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a group</td>
<td>/api/groups</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a group</td>
<td>/api/groups/id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create data classification</td>
<td>/api/data-classification</td>
<td>POST</td>
</tr>
<tr>
<td>Get a data classification</td>
<td>/api/data-classification/id</td>
<td>GET</td>
</tr>
<tr>
<td>Get all data classification</td>
<td>/api/data-classification</td>
<td>GET</td>
</tr>
<tr>
<td>Edit data classification</td>
<td>/api/data-classification/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete data classification</td>
<td>/api/data-classification/id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a data map</td>
<td>/api/data-maps</td>
<td>POST</td>
</tr>
<tr>
<td>Get a data map</td>
<td>/api/data-maps/id</td>
<td>GET</td>
</tr>
<tr>
<td>Get data maps</td>
<td>/api/data-maps</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a data map</td>
<td>/api/data-maps/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a data map</td>
<td>/api/data-maps/id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create data item</td>
<td>/api/data-items</td>
<td>POST</td>
</tr>
<tr>
<td>Get a data item</td>
<td>/api/data-items/id</td>
<td>GET</td>
</tr>
<tr>
<td>Get data items</td>
<td>/api/data-items</td>
<td>GET</td>
</tr>
<tr>
<td>Edit data item</td>
<td>/api/data-items/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a data item</td>
<td>/api/data-items</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a data subject</td>
<td>/api/data-subjects</td>
<td>POST</td>
</tr>
<tr>
<td>Get a data subject</td>
<td>/api/data-subjects/id</td>
<td>GET</td>
</tr>
<tr>
<td>Get data subjects</td>
<td>/api/data-subjects</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a data subject</td>
<td>/api/data-subjects/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a data subject</td>
<td>/api/data-subjects/id</td>
<td>DELETE</td>
</tr>
</table>


### Authors
- Arnold Osoro - [mmosoroohh](https://github.com/mmosoroohh)
