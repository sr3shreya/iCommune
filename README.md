# iCommune
Console based Chat Application using Python and Firebase Realtime DB
####################################################################
                  ####Firebase Setup#####
####################################################################
1. Create a Project in Firebase
2. Enable Googel Analytics - Optional
3.Select account (Default Firebase Account)
4. Add Storage (optional)
####################################################################
                      Add Web App
####################################################################
1. Create New Web app
2. Hosting( Optional)
3. register App
####################################################################
                    Config for Python
####################################################################
1. Go to Project Settings
2. Scroll down and copy Config in your python code
3. Copy DB URL and add -
    "databaseURL": "URL to YOUR DB"
#####################################################################
  Create Service Account - Generate private key for authentication
#####################################################################
1. Go to Project Settings -> Service Account
2. Under FireBase SDK , select language (Python in this case)
3. Copy the code snippet for app initialization 
4. Generate New private key
5. Save and add path to your JSON in the code snippet
######################################################################
              INDEXING and Database Schema
######################################################################
1. For applying Rules on your DB, Refer to the Index.json
2. For DB Schema Refer to DatabaseSchema.json
