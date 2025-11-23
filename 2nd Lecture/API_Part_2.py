# API Part - 2

# Agenda : 

# 1.PUT : Put means Update
# 2.DELETE : Delect means Delect



# 1.Put : It means update the operation, Lets say we have a data, we have the record, I would like to update those record. In that case
# I can send the request as a "PUT" request and

# 2.Delect : 2nd option is lets say I have delect some of the record.
# So, in that case, I can send a delect request.




# Start Coing :

# Lets Import from "Fast API"
# Then from "Pydantic" import "BASEMODEL"

# We have to import 2 things over here,"Fast API" & "Pydantic".

# "Pydantic" used becasue it used for Data Validation.So, whenever we are sending a data, it will try to validate it with
# the help of Pytdantic class. So, this is something we try to follow inside a "FastApi". And now a days it is very normal,
# in a pythonic Framework.

# whenever we go through Lama index, Langchain & Even a Crew AI. which will help out to creating an agents. Almost everyone is
# Following a "Pydantic", going forward we will going to see such things alot.   

# Note :

# Data validation, we are going to use it. Means whatever data type, we are going to define, whatever ranges of the data we will 
# be define, So, "Pydantic" will be able to validate beforehand.

# Now, lets create the Variable of "Fast API". SO, this is my -> Variable ["App"], we can say object of "FastApi" class.
# We are able to create, which will going to help me out to expose anything as an API to anyone.

# Now, I am going to put method, "PUT" means update, so what we are going to update here is that,  we need some sort of data,
# If we have to update something, onviously I need a data, unless and until I dont have any data, what I am going to update,
# This is possiblity that data is avaiable into databases, maybe data is avaiable in a file system.
# Maybe I can create data over here itself.



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1:{"name": "vijay", "age": 30},
    2:{"name": "Ajenkiya", "age": 25},
    3:{"name": "durga", "age": 28}
}




class User(BaseModel):
    name:str
    age:int



@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message" : "User updated successfully", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}
    
print(user_db)

# Lets say [ "User_db" ] = just a dummy data, I am going to create over here, 

# 1st User :

# Maybe user Id I have  : 1, for that Maybe I have,
# a name over here, name is = to "Vijay", & Age = 30 

# 2nd User :

# name = "Ajenkiya" and age = 25 .

# 3rd user : 

# Name = "Durga" age = 28 

# This is a sample record which I have craeted over here.
# We will try to update this record, as we can see this record in a "dictionary" format,
# I am holding a data in a "Key" "Value" pair.
# Key = 1 which is ID lets suppose &
# entire this dictionary is Value = {"name": "vijay", "age": 30},

# Inside this Dictionary again, we have a "Key" & "Value" pair.

# This format way, I want to keep my data, we can even create or must having "Dir" inside "Dir" again inside "Dir".
# Depends how we keeping our data or how we are holding our data, we are having complete control to it. But yes we will take 
# simple sample data and lets do it. May be I will try to update this data, with the help of this "PUT" request. I will try to 
# update the data.

# Note : 

# Now, we have already created this "user data", now we have to update the data, obviously we will have to use the "PUT" method.

# For this I will create the function. That function will upadte my data, & that function I am going to eventually open it up
# as an "API", this is the meaning of an API.




# Code below : 

# class User(BaseModel):
#    name:str
#    age:int

# Now, here we have to create a class, lets say. So, that it will be able to take the data and 
# It will be able to do a data Validation. So, class call as a "User" , we can give any name, and we are trying to "Inherit" 
# the ["BaseModel"], So, that It will be able to get all the property of the base model class a "Pydantic" Class.
# So, here we have a user, inside this user lets say we have a name it should be avaiable as a "String" &
# we have a "Age", it should be avaiable as a "integer".

# Basically, we have ["Name"] & ["Age"].

# Only this dataset we have, so we are looking for validation for this 2 dataset.



# Code Below :
# def user_update(user_id:int,user)



# Lets suppose, we are going to create function over here, I will going to write the, 

# Code Below : 
# def user_update.



# This is the function, which I am going to create. Again, when I am trying to update the user, so obviously I have to pass
# the value, that which user I would like to update, Maybe User 1 or User 2 or User no 3?

# So, we have to pass those values, ok "User no 1" I would like to update, "User No 2" , I would like to update, Then I have to
# pass the our upadted data as well, both the data.

# what this Update function will be do, It needs a user ID, means which ID, I need to upadate, Then against that, 
# I need this data. - 2:{"name": "Ajenkiya", "age": 25},   then only I will be able to update the data, 
# Lets suppose, I want to upadte the ID No.2  -> 2:{"name": "Ajenkiya", "age": 25},  means ok what is the new data, this is the
# old data, -> 2:{"name": "Ajenkiya", "age": 25},  | So, what will be the new data for the USer ID : 2?

# So, that data also, I have to pass, that data I can pass via a "Pydantic" class.


# Code Below : 
# def user_update(user_id:int,user:User)



# So, here as a parameter, I can say, I am going to pass the "User_ID" as a "Integer" lets suppose, then I am going to pass as a
# user data now. So, here "user:" data is coming from where? from my "Pydantic Class" -> this one - [ "class User(BaseModel)" ]
# a Capital "U" User, That I have created, Means Validate it and Pass it, This "Pydantic Class" is taking "Name" & "Age".

# Yes, the "Name" and "Age" is required inside my dataset.
# Here we will try to pass an "ID" that which one to Update, then equivalent dataset, for that "Particular ID",




# Code Below : "IF"

# if user_id in user_db:
#        user_db[user_id] = user.dict()
#        return {"message" : "user updated successfully", "user": user_db[user_id]}




# Here inside this, we can keep the check, we can write my be "If" statement, If user ID exit do this, 
# If User_ID does not exit, do that kind of Statement. 


# Id user_Id is in User_db : 

# If the User_id is in the that "User_db", then basically update the "User_db", for that Particular "User_Id".
# Then Try to update the basically, update the [User_db] for that particular User_id with this data ["user.dict()"],
# whatever the data that, we are getting, means we are geeting the data from here - ["user:User)"] this captital - U "User"
# SO, we are trying to extract those data ["user.dict()"], then against that ID, ["user_db[user_id]"] we are going to update it.
# Then, now return you message - [""] ok, as I have user Updated successfully, we can write anything, in return,
# Here, as we have written,  a returning a message : ["User_updated Successfully"] - 
# with this particular, user ID -> {"User": user_db[user_id]} it has been updated.

# This is something we was trying to do. Based in this condition.



# Code Below : "ELSE"

# else:
#     return {"message": "User not found"}



# If this is not going to happend, then we can try to write the "Else Statement", or parallel "return" over here, do this.

# "Else" return a "Message, User not found".  So, whatever User_ID that we were trying to enter that user does not even exit.
# If the User does not exit, then what I will do, I should not append any new data, I should always updated.

# Note : 

# This is my simple and plance "Function", which is going to update my this dataset that I have  
# This one -> 
# 
# user_db = {
#    1:{"name": "vijay", "age": 30},
#    2:{"name": "Ajenkiya", "age": 25},
#    3:{"name": "durga", "age": 28}
# }




# Note :

# I have to expose this function, whihc I have, So that from any programing language and any other "framework" we will be able 
# access it.

# Currently this is inside my system and I wanted to expose it to other program in my local system.

# This is the Meaning of "API"




# Below Code

# @app.put("/user_db/data/v1/update/{user_id}")
# def user_update(user_id:int,user:User):
#    if user_id in user_db:
#        user_db[user_id] = user.dict()
#        return {"message" : "User updated successfully", "user": user_db[user_id]}
#    else:
#        return {"message": "User not found"}




# So, what we need to do, we just have to call the [ "@app" ], & what I will call, so this time, I will call the ["PUT"],

# Why "PUT, this time, I am trying to create this function for to update the user, So I called the ["@app.Put"], so that 
# I can update the user.

# Now,  I would like to create the "Route" means at this location, you will be able to access this particular function.

# The user update function, which I have written, "Route" depend upon me, any "Route" I can give any kind of "Route" I want.

# So, here simple I will write the ("user_db/data/v1/update ") <- something like this. I have given the "Route" means
# If you will go through this "Route", then only you will be able to update.

# This is my Route, I give short or long Route it totall depend upon me.

# when we are using a ("PUT"), then we after this Route -> ("user_db/data/v1/update "), we have to pass a "user_ID",
# we can Parameterized over here, saying that ok, I will try to do a Update, for this particular "user_id".

# In this Route itself -> ("user_db/data/v1/update/{user_id} "), I am sending the this data {user_id}.

# You can append {user_id} as a parameter, so this is -> {user_id} nothing just a parameters.So, that it will be understand that
# which record, I have to update, 

# In this "Route" itself, -> @app.put("/user_db/data/v1/update/{user_id}")   I am going to send a which record we have to update
# as a parameter.

# This line code -> [ def user_update(user_id:int,user:User): ] <- As a data (user:User), I am suppose to send this data ->
 
# name:str &
# age:int)

# Technically this information, -> [ 1:{"name": "vijay", "age": 30}, ] I have to send, Against the ["{user_id}"], so that it
# will get those data -> [ "user.dict()" ] & then it will be update it -> ["user_db[user_id]"] against that paricular [user_id],
# which I am sending
# So, here -> (user:User), I will try to send a data inside my body.

# So, This is the philosophy behind the ["PUT"], update this one -> {user_id} & keep the Route whatever we want 
# -> "@app.put("/user_db/data/v1/update/"


# So, lets run this file, how we can do this open the Terminal and -> similar way "Uvicorn"

# So, code is -> uvicorn testing:app --reload 
# --reload means so that it will reload again & again itself, it will not ask any unnecessary when I am going to make any change.
#  















# Lets Start Executing my code

# 1st lets Save it CTRL+S and then I define my path : 

# cd C:\All_Important\Generative_AI_Euron\API_Part2 & 
# python Api2.py

# Next is we will be run by the "Uvicorn"  & my file name is ("Api2") column (:), --reload.

# This "--reload" will automatically update not going to ask again & again for the update or changes.
# so, my code will be [" python -m uvicorn Api2:app --reload "]
#  As we can see it working with out giving me any error.

# So, we have written entire Function and we have expose it to the entire world.

# As we can see my app is running here this URL : [" http://127.0.0.1:8000 "] at this Local host -> ("8000").

# Now If I have to access it and need some sort of update or changes then, 

# Open the Google and paste this -> [" localhost:8000 "] and provide the "docs". SO complete URL -> [" localhost:8000/docs "]

# As we can see this opened and this "Swagger API", Now as we can here, there is a ["PUT"], request. which we can see here as "UI",
# In the "swagger API" -> To execute it this is the same command we have provide, which  we have already done previous lecture.

# Note :

# So, here in this "Swagger API", we can see the ["PUT"] & now lets suppose, I have to test this "API" then, 
# Here, I have to put the "User_id" lets say I put [1] means this one 1st record I am putting -> [ 1:{"name": "vijay", "age": 30},
# I can put [2] or [3] then that means it will update the 2nd & 3rd records. 
#  & Now "Request body" or Content, inside we need to write this.

# "name":"gurung",
# "age" : 40 

# This is something I am going to pass and execute this code, as a outcome, we can see it is successfully giving me the ouput.

# So, by looking my output, we can see that we have written the Function like that way -> 
# code : return {"message" : "User updated successfully", "user": user_db[user_id]}

# "User updated successfully" & the user id or details, it is going to return. data basically -> "name" & "age"
# So, as we can see outcome, we are able to successfully update a record.


# Next,

# Let's suppose I would like to print and update the data somewhere, 

# Just add 2 more line of code -> 
# Just below this code add the ->  [ user_db[user_id] = user.dict() ]
#  Add this one -> [ Print(user_db) ]

# Then at the end put this line of code  -> [ " print(user_db) "]
# 

# Now, save this code "CRTL+S", Go to the "Swagger API" and hit the API & and same input just execute it.

# Inside the terminal as we can see the oucome :
# -> {1: {'name': 'gurung', 'age': 30}, 2: {'name': 'Ajenkiya', 'age': 25}, 3: {'name': 'durga', 'age': 28}}

# "Vijay" name change with "gurung", we can see the changes outcome, below this terminal. why because.

# Inside the "Swagger API" inside content box I have written this dictiony - "Key and Value"

# This below code :

# {
#  "name": "gurung",
#  "age": 40
# }

# Below the terminal, we can see the lastest changes.

# Name = gurung
# age = 40

# whatever update, I want to send, with repspect to the particular ID. I am able to get that particular data.
# Simple means, I am able to upadte the record, that was the whole object and idea.



# Next :  "POSTMAN"

# NOw lets try to test it with the help of "POSTMAN". Open the "POSTMAN"

# If I will come to a "POSTMAN", if I have to hit my API, So, They Type of request is ["PUT"] over here & then basically 
# we have to provide a "URL", where our data is present & then, we have to pass the data.
# This is my Route -> /user_db/data/v1/update/.

# Lets say we are trying to update the record number [2], then so in the Route we will add 2.
# PUT = http://localhost:8000/user_db/data/v1/update/2  

# Datawise, we will provide something like this -

# {
#    "name":"datascientist",
#    "age": 10
# }

# If we hit enter or send inside "POSTMAN", now we can see it upadted successfully and changed inside my "POSTMAN", we can see.
# As we can see User name is changed successfully and User name is = "datascientist" which I have provided,against basically
# my user_ID 2, I have updated this particular record something like - Datascientist and 10.

# If I will check below my "Terminal" as we can see it is changed successfully. There new record whihc has been updated.

# This record I am trying to upload in my Local, but lets say I have a database and I can go ahead and try to update the record.
# Maybe I have a some sort of "JSON", file or may be a "CSB" file or maybe "TXT" file.That file if I would like to do something.
# everyehre I will be able to do it. End of the day whole idea was to ["PUT"] & with the help of "PUT", 
# update the some of the records.


# Note :

# Difference between "PUT" & "Patch" :

# There is anothe Method called the Patch.
# So, ["PUT"] will try to upadte the entire record, against whatever "KEY" & "Value" that we are trying to do something.
# PUT will be try to update the entire record, update full records.

# ["PATCH"] - As name suggest, what Patch will do is, Patch means we are trying do a Partially, we are trying to apply a Patch
# on the Top of something, Patch will help out interms of updating the record, but partically.

# Both, will going to help out interms of updating the records.









# 2.DELETE Operation :


# Let's try to understand the ["Delete"] operation.

#  "Delete" means it will try to delect something records, this is the actual meanining of it.

# So, lets write a function, 

# Def Delete underscore User function. To delete any user function, I have to pass any "User_id as Integrer (int).
# Then it will check if User

# def delete_user(user_id:int):

# Code Below : 


@app.delete("/user_db/data/v1/delete/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return{"message": "User deleted Successfully"}
    else:
        return {"message": "User not found"}





# 1st line code : Explanation : 


# 1st Line code :  def delete_user(user_id:int):

# so, I will write something like def delete_user function, Now to delete any user I just have to pass the user_id, so User_id
# I am going to pass, User_id as a integer, "int"
# 1st line code :
# 

# Now, it will try to check User_id in User_db, if user_id in User_db, So, user_id exists,
# Let's suppose, I have passed "User_id = 4", but that is not even avaiable in our data, inside my "User_db" only upto 3 records
# is avaiable there. So, what it will delete nothing.It will not able to delete anything.
# So, This line code just try to check that, "User_id" in "User_db", if this line code is True, Then it will try to call the
# delect operation, this is how anything is delected in Dictionary.


# Code : 

# if user_id in user_db:
#    del user_db[user_id]
#    return{"message": "User deleted Successfully"}


# Just go to the "Practise.ipynb" and write the code

# So, practically we saw, same dictionary opertaion here we are trying to perform.

# "del user_db[user_id]" , whatever User_id, we are going to pass.Then return a message whatever we are going to pass.
# As we can see "User deleted Successfully".

# else:
#     return {"message": "User not found"}

# If the "User_id" did not found or exit, then it will fall inside "else" statement. & It will return the "User not found".

# Now, if I have to convert this delect function whole code into a "API", we know the simple
# just @app.delete & provide Route something like this -> ["@app.delete("/user_db/data/v1/update/{user_id}")"], 
# whatever route, we would like to give & it will perform the operation.
# Now lets test this "delete" operation in "Swagger UI"


# Before this just provide the path -> 
# cd C:\All_Important\Generative_AI_Euron\API_Part2 
# python Api2.py
# python -m uvicorn Api2:app --reload

# Now copy this URL and paste on Chrome -> [ "http://127.0.0.1:8000/docs" ] As we can see this is opened.
# Now as we can see here, we have "PUT" request is there and "Delete" request is there.
# Now lets test with "Delete" one.

# Now lets Pass "User id" Lets say [2] & execute it. 
# As a response I am getting "user delected successfully", 
# lets say I will give "User_id" lets say [7] and execute, as a outcome we can see message return -> ["User not found"].

# Similary we can test same thing in the "curl" or in "POSTMAN"

# Lets try in "POSTMAN" 
# So Select -> Delete : URL -> [ http://localhost:8000/user_db/data/v1/delete/3 ], this 3 is my "User_id" that I will give.
# Select ("Body") & select ("None")
# Message we can see that "User delected successfully", Now if i will do again again, this time message appear different
# Because we have already delecetd the 3rd record, so message will apear -> [""message": "User not found""], But inside my
# terminal it showing 200 Ok status.

# Note :

# while sir was writting code, automatically code written or suggestion, to install it
# Here in the VS code Extension section, there search "Github Co Pilot" & then enable that.

# So, finally we have completed both ["PUT"] & ["DELETE"] Methods.










# Now Deployment :


# Now lets deploy this into a cloude platform, As of now this is running into my local Host


# Note : "Ngrok"

# There is one "Port Forwarding" last class we have discussed, what does this meaning?
# ["Port Forwarding"] means if something is running on my local Host, on some particular port URL
# SO, with the help of the "Ngrok", we was able to expose to the entire world.

# with the help of "Ngrock" anyone will be able to use it, test it and able to use my "API".

# Note :

# But lets say I dnt want to keep anything inside my local system, I just want all of this things, on some server or on
# some of the Cloude platform, How we will be able to do a Deployment of this entire API.

# Whatever is running inside my Local server, it should not available in my local system, It should be avaiable in some of
# the Global platform, anyone able to access it without any Tunneling or withour any "Port Forwarding"

# To do that, obvioulsy we have to deploy the solution any of the Cloude platform.

# so, there are many clode provider for example -> AWS, GCP, Azure etc major provider and there any many more...

# So, this is my local machine and if we deploy on cloude that is public machine. Whatever is running here in my local machine
# Same thing If I will run in the CLoude platform, all will be able to access it.This is what deployment means.

# Note :

# Cloude platform will not be having any idea that, what types of dependency and what kind of instllation it has to do.
# we have to mention it.

# SO, incase of the Python Project we have to create one file name is ["requirements.txt"]
# Inside this "requirements.txt" I will going to add all libaries that I have used.
# These was the 2 libaries that we have used - 
# 1.fastapi 
# 2.uvicorn

# Next ,

# Now, we have to choose the cloude platform where we can do a Deployment, before that we have to push our code into the 
# "Github" then only we are able to do a deployment.

# Lets say if we choose AWS, GCP or Azure, we have to add the credit Card so I am going to Choose the platform for my deployment
# is ["Render"] which is free and I am able to deployment.

# Next,

# NOW this go to Google and search for "Render" URL : [ https://render.com/ ]

# I have logined in with Gmail now, this "Render" provide a Machine, where we go and 
# the we are able to productionize our application,means whatever is working in our local system, we can put that in a Render
# & it is going to give me a Shared Instances, Means there will be a big Machine which will be shared by multiple people
# There is a payment potion, If we are go and attached the Payment option, then it will try to give us more facilities
# interm of scalling, security etc, 

# So open 2 Tabs, one is "Render" & another Tab is "Github account".

# So, we are going to push the code into the Github, once we are able to push our code into the Github.

# Timing - 1:09:06 
# 
# So, we are going to Push our Code into the "GitHub", once we able to push our into the GitHub then, we are going to
# attached those inside a "Render" & that will be Deployed.
# Now to push something into the "Github"


# Note : 
# To check Git is avaible there or not? Just open "Command prompt" type - git  & hit enter and my case already there.


# Next : Steps : 

# Now we have my "Api2.py" & "requirements.txt" file, I have to push this code which is aviable inside my local device
# to a Github. "Github" which is nothing but code repository.
# Steps :
# From "Local device" to "Github" & then next to we will call inside the "Render Cloud".

# This is the steps we will going to follow, -> I have successfully tested inside my "Local system" and my "Github"  is ready,
# Now "Render" we will going to login and all these 3 components are ready.





# Github : 

# Steps Follow inside "Github" 

# Click on Profile of Github and there is option call [ "Your Repositories" ] -> [ "New" ] -> I will name it -> ["Api2"]
# now create ["Repositories"].

# Now the movement, I click on create ["Repositories"], I will get the -> ["or create a new repository on the command line"]
# Now this commands will help out to us to push our code, into a Github repository.
# Here, only 4 to 5 commands is there we have to use it, from next time 2 to 3 commands we will have to use.

# Details Explained for Understanding :
#
# 1.git init : Here, we have to initialize the Git, 
# 2.git add:  Here, we have to try to add our file into buffer memory, inbetween "Github" & our local, technically in our local.
# 3.git commit :  Here, this mean just sent some sort of a message.
# 4.git branch : Here, Branch means, the Branch where we try to send our code.
# 5.[ https://github.com/Vijaygurung1/Api2.git ] : Here, this is nothing but, its a URL, we can see in our brower, that has been 
# Create the movement, I have name it as a "Api2" one URL generated, this is the same URL, what we mean, this url is for this
# repository, where I have to "Push" the code.
# 6.git push :  Here, this is nothing but final Push the code.

