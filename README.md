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
<td>Create an asset</td>
<td>/api/assets</td>
<td>POST</td>
</tr>
<tr>
<td>Get an asset</td>
<td>/api/assets/asset_id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit an asset</td>
<td>/api/assets/asset_id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete an asset</td>
<td>/api/assets/asset_id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a process</td>
<td>/api/process/process_id</td>
<td>POST</td>
</tr>
<tr>
<td>Fetch a process</td>
<td>/api/process/process_id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit</td>
<td>/api/process/process_id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a process</td>
<td>/api/process/process_id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a group</td>
<td>/api/groups</td>
<td>POST</td>
</tr>
<tr>
<td>Get a group</td>
<td>/api/groups/group_id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a group</td>
<td>/api/groups</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a group</td>
<td>/api/groups/group_id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create data classification</td>
<td>/api/data-classification</td>
<td>POST</td>
</tr>
<tr>
<td>Get a data classification</td>
<td>/api/groups/group_id</td>
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
<td>Create a report</td>
<td>/api/reports</td>
<td>POST</td>
</tr>
<tr>
<td>Get a report</td>
<td>/api/report/report_id</td>
<td>GET</td>
</tr>
<tr>
<td>Get report</td>
<td>/api/reports</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a report</td>
<td>/api/reports/report_id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a report</td>
<td>/api/reports</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a data input</td>
<td>/api/data-inputs</td>
<td>POST</td>
</tr>
<tr>
<td>Get a data input</td>
<td>/api/data-input/id</td>
<td>GET</td>
</tr>
<tr>
<td>Get data inputs</td>
<td>/api/data-inputs</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a data input</td>
<td>/api/data-inputs/id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a data input</td>
<td>/api/data-inputs/id</td>
<td>DELETE</td>
</tr>
</table>


### Authors
- Arnold Osoro - [mmosoroohh](https://github.com/mmosoroohh)
