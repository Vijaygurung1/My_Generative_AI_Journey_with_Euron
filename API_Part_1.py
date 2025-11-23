# API - Part - 1

# Create API
#- we will going to create API and we will going to Test an API.
# - When I am going to create an API there is an
#- 1.GET Method, 
#- 2.POST Method,
#- 3.Put Method,
#- 4.Delet Method.

#- One by One we will going to discussed this.

#- To execute or create this API, I am going to use the Framework or libary called the Fast API Libary.
#- Use Flask, Django anything is fine.


# Note :

# - To use this 3.10 python version, we need to install "ipykernel" as a [ pip install ipykernel ]

# Install Some Frameworks or Libaries.

# 1.Fast API : pip install Fastapi

# 2.uvicorn : pip install uvicorn : This is because, so that we will be able to execute the Fast API.

# pip install ipykernel



# pip install uvicorn


# Import FastAPI

#- Here, we have to import FastAPI :  from fastapi import FastAPI.
#- once we are able to import fastAPI, then we have to create an Object of Fast API. But lets forget about leave it as of now.


# Create Function -

#- Lets suppose, I am going to create an Function, add function or addition function.
#- What Addition function will do, it will take 2 input (a,b) & it will going to return ( a & b ).

#- add(3,4)
#- If I have to call this function in this program itself. Then I am going to pass the value of (a,b) or (3,4).

#- Now, I am going to execute this entire things. As a result we can see we have got 7 over here.
#- This is a simple Add function, we have written.

from fastapi import FastAPI



def add(a,b):
   return a+b

print(add(3,4))

# Note :
# - If I have to executive this FastAPI juts CTRL+Save. or Open Terminal Type: [ Python test.py ] 
# But, my case open terminal and type this [ cd C:\All_Important\Generative_AI_Euron\API_Part1 ] next # python Api.py

# - if we want to clear below inside terminal this just type : "cls" it will remove all.

#def add(a,b):
#   return a+b

#print(add(3,4))

# Question : expose to ourter world.

#- This is Python program and I am able to access it and it working perfectly fine. 
#- But now someone has asked to expose this function to the outer world, so that anyone will be able to access this function, from 
#- any framework, or from any program or from any URL, or from Google chrome, they should be able to access it, we will be able to get 
#- the output, How to do it.
#- So, that this API concept comes to picture, we have discussed in theory that that Bank hit through Gpay and all.

#- So, here I have to expose this function to the outer world.So that if somebody request it should get access. 

# Create object :

#- How I will be able to expose this particular function, lets try to understand it.

#- FastAPI is framework that, I am going to use, lets say I am going to create one object, which means Variable, of FastAPI.

#- I am just trying to call the FastAPI()  & this is the variable is app [ app = FastAPI() ], so that I will be able to access this
#- entire libary.

#- Now, what I will do with this Variable, & how I will going to expose this function "def add(a,b)": to the outer world.
#- @ <- call this Decorator. Decorator will give an access or power then @app.get("/") slace (/). This is something we have to write.
#- with the help of this line of code : @app.get("/") , Now I am trying to clame, this function -> [ def add(a,b) ] : is expose & 
#- API has been created. This is what we was talking.

# - Now below line of code, how will be Test it.
# - Now if we have to execute this, we have to call the "uvicorn" libary, that we have already install it.

# Below is Sir code, which is not working my code, So I am using my own code.
# from fastapi import FastAPI


from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def add(a,b):  
    return a+b

print(add(3,4))



# Note :
#- If I have to executive this FastAPI juts CTRL+Save. if we want to clear below inside terminal this just type : "cls" 
#- it will remove all.

#You need to first move into the correct directory and then run the file:
# cd C:\All_Important\Generative_AI_Euron\API_Part1

# python Api.py


#- Now if I have to execute this code. just open Terminal 
#- and type inside Terminal ->>>>    [ uvicorn Api:app --reload ] or my case this is working - ["python -m uvicorn Api:app --reload"]
#- [ uvicorn Api:app --reload ] or ["python -m uvicorn Api:app --reload"]

#- So, that it will reload automatically, whenever I am going to make any changes in my code. So, I dont have to execute this file or 
#- function again and again.  make sure it is in the same Directory, basically my code location. 
#- Now the movement, I will execute this inside my terminal. If it execute perfectly then we can see message that -
#- Info : will wathc in changes in the directroy and Uvicorn is running in this URL: http://127.0.0.1:8000  etc,message we will going to see.
#- Where i have a IP Address and Port Number. 
#- This IP address : URL: http://127.0.0.1:8000 technically IP address of my local system. If I will going to Host it in the other server,
#- then the IP addres of that Public Server. IP adress is nothing but its an Address for any system. 
#- "Port number" is nothing but we are running a program, lest say this "[python Api.py]"
#- Now in our system, we have a series o the port. from 0 still milion. inside our system.
#- This progrm is basically exposed to that Ternnel, that particular Port.
# With the help of this URL: http://127.0.0.1:8000 / If I will hit this URL, Currently it is running live now. If this is not 
# running that case we cant hit this URl.SO, it should be keep up on running all the time.
# If I will hit this URL or IP Address : http://127.0.0.1:8000  - with this IP Address [http://127.0.0.1]- with this I am reaching
# out to my local system, where I have execute this program, inside this system at this Port -> [:8000 ] number, my code that I have
# written is Up in running.this method is actually live : 
# def add(a,b):  
#   return a+b
# I have written here in code : @app.get("/") <- what this (/) slash meaning.



# Now, my program is live, I will copy this program : [ http://127.0.0.1:8000 ] & open browers and paste it. we are able to see 
# something, now what we have to do over here is that. [ http://127.0.0.1:8000/docs ] just add -> (/doc), if we hit enter, now 
# we are able to see a "UI", this UI is called the "Swagger UI". So, FASTAPI, provide Swagger UI as well.
# This "UI" helps us testing, we have mutiple way of testing but, we are able to see here ["GET"] & This is our own function ["Add"]
# This is the function ["Add"], which I have written. & at this root (/) slash, this function ["Add"] is avaiable. Where it is taking
# 2 input "a" & "b"  & lets provide value or a = 4 & b = 5 and execute the code. 1st click "Try it out" right side and put the value
# Lets say I execute this code multiple times, "Execute", then we can see that we are able to see some short of output.
# As a output it is giving me ["45"], Why giving me 45?
# whenever, I will try to give or put value in a = b = it is trying to consider as a "String". I have used (+) so it is consider,
# Concatenation operation. That is again a Problem, It is trying to perform "Append Operation".
# So, How we can mitigate this kind of situation, when It execute my method, inside my console it was giving me (3+5), it was 
# trying to do a Addition operation.
# But when I try to send a data through this URL - [ http://127.0.0.1:8000/docs ] / GET, Here a & b it is trying to consider as
# a & b type as a "any", & bydefault it is consider as a "String" & so I am able to (45) as an ouotput. anyhow it is giving me data.
# But, how I am going to make sure that, it should consider, ["Integer"], it should not consider this a & b as a ["Any"].

# Note: 

# Now lets make changes in code, lets make it from any to ["Integer"]. I made changes in code.



from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def add(a:int,b:int):  
    return a+b

print(add(3,4))


# Just save the CRL + Save - (--reload ) <- this is meaning of this line code 
# and go back to Browser and Refresh it and we can see that, it change to "int" 
# Now, lets execute a = 4 & b = 6 over here and we can see that, we are able to see the 4+6 = 10 as a outcome.

# With the help of this "UI" what technically happening is, our function is live at this particular location : ["http://127.0.0.1:8000"]
# & we have written this function will be avaiable at this (/) slash, this is the Route @app.get("/") basically we are trying to give.
# let's say this function will avaiable at this "Vijay" route. I have given my name lets say.


from fastapi import FastAPI

app = FastAPI()


@app.get("/Vijay")
def add(a:int,b:int):  
    return a+b

print(add(3,4))


# Just CRL+save it and open Browser and change URL to "Vijay" -> ["http://127.0.0.1:8000/Vijay"] <- hit enter & 
# ["http://127.0.0.1:8000/Vijay/docs"] <- hit enter. Final URL -> ["http://127.0.0.1:8000/docs"]<- hit enter now it changed.
# Now, it showing me Route = "Vijay"

# Note :
# Let's Say,
# I am going to make change in my code @app.get("/Vijay/gurung/xyz") again and CTRL+Save it and 
# open browser and refresh it and we can see the change.


from fastapi import FastAPI

app = FastAPI()


@app.get("/Vijay/gurung/xyz")
def add(a:int,b:int):  
    return a+b

print(add(3,4))



# Note : 
# What is the meaning of this - ("/Vijay/gurung/xyz" Add ) <- this mean 
# This "Add" function is avaiable, which location, it is aviable to this IP address :  ("http://127.0.0.1") - which will help me
# out to reach out to the system. Inside this Route, at this location -> ["/Vijay/gurung/xyz"], mean "directory inside dir" 
# "inside directory"  consider that way.  This is technically -  ["/Vijay/gurung/xyz"] called as Route.
# What is whole Route to Hit this function - ("Add")?
# This is technically Route or API - ["http://127.0.0.1:8000/Vijay/gurung/xyz"], by which we are reaching out to this function 
# this function called as ("Add").

# Note : 

# Why Docs? and what use of it?

# So, basically "FastAPI" provides a UI, so that we can test it with the UI itself, that reverage we get with the "Fast API".
# what is the input and output we will be able to see and we can test it.
# wherever our API is running, just do a "/Docs" and we will be able to access the UI.
# Through UI, we will be able to do a Testing.

# Note :  

# [ http://127.0.0.1:8000/Vijay/gurung/xyz ]

# Let's suppose, I dont have a UI, in that case what will do. My function is running at which location. This is the location 
# where my function is running ["/Vijay/gurung/xyz""]

# This is the my Total Route -> ["http://127.0.0.1:8000/Vijay/gurung/xyz"] open tab and paste it and hit enter.
# It is giving me some sort of detail, in this Key : Value pair, this code it is telling me you have to pass a value of "a & b".
# That is something you will pass then only, I am able to execute it. 
# If I will hit this same URL multiple time and come and check below Terminal, 
# we can see the message that ["422 Unprocessable Content"] <- whenever We try to hit this ["@app.get("/Vijay/gurung/xyz")"] path.
# It is trying to execute this add function  : 
#  def add(a:int,b:int):  
#    return a+b
# To execute this function, I need to input the value of "a & b".

# How will, I pass the value of a & b. So, that I can try to execute it.

# We have see that, with the help of "Swagger UI", which we was able to access, (/docs), where i get the UI and I was able to 
# test my API.

# Note : ["URL itself "]

# [ http://127.0.0.1:8000/Vijay/gurung/xyz?a=4&b=5 ]
# Let's understand with the help of URL itself, how I will able to execute it, lets understand

# At this path -> ["http://127.0.0.1:8000/Vijay/gurung/xyz"] my function is avaible, So, I will write -
# ["http://127.0.0.1:8000/Vijay/gurung/xyz?a=4&b=5"] add this ("?a=4&b=5") <- If I execute this. we can see that I am able to
# get my output is (9).

# Through a broweser, I am able to execute my python code, as a outcome we can see down below in terminal, we are getting 200.

# 1.With Swagger UI - we was able to get the output
# 2.With Broswer  - Again with the help of Broweser also we are able to get the outcome.

# SO, we understand how we are able to reach out to this function :
#  def add(a:int,b:int):  
#    return a+b
# what is the meaning of this Route and URL -> ["@app.get("/Vijay/gurung/xyz")"]

# I am able to reach out to this function and able to execute it.Technically,this is my APY -> ["http://127.0.0.1:8000/Vijay/gurung/xyz"]
# & I am trying to pass the data.

# this is my API -> ["http://127.0.0.1:8000/Vijay/gurung/xyz"] & If I am going to expose this API to the entire world.
# So, that Anyone through this URL can access anyone API. I will be able to access anyone "Add" function through this, basically
# anyone local system.
# Note : There is tool call "Ngrok" google it. with the help of Ngrok, I will be able to do that.
# 1st we have to download it and then with the help of "Ngrok", we will be able to expose it.

# Note : 

# "NgRok" "URL -> [ https://ngrok.com/downloads/windows?tab=download ]"]

# So, Basically this is small file, just open in Command prompt, for that step:
# Go to the file location. above path, "C:\All_Important\Generative_AI_Euron\Ngrok" remove it, just type "Cmd" hit enter 
# it will open in command promp and - type "dir" the it will redirct me to the Prompt.
# Now type : 'Dir" we can find the - "Ngrok.exe" file is avaible inside the dir file.
# What next, so my entire things is running inside my port - ["http://127.0.0.1:8000 ] we hvae to make this port and my system,
# expose to the outer world means to everybody over the internet, so that anyone can with teh help of this URL can test it
# by there own computer. I am making my local machine to Global. 
# So, that is why "Ngrok" comes to a picture. everybody able to access it by a URL given by "Ngrok"





# Command :  Continue type inside command
# 1.dir 
# 2.ngrok http 8000 -> 







# # Login inside "Ngrok" email pw - and copy this Token and paste inside teminal 
# Token :   ["ngrok config add-authtoken 3249bGX8MkdwnRSYcVjXDd7CRn9_7gmau886b6wjX37z4tdBg"]

# ["ngrok type HTTP why because it running in a local, not in a Https & then it running in a port No."8000"
# By doing this I am saying that lets try to make it Global, means whatever running in my "8000" the "Ngrok" will try to
# expose it to the entire world.]
# The movement I type this -("ngrok http 8000") & hit enter new tap will open in terminal.
#
# This is my local Host : ["http://localhost:8000"] &
# This is the Https : [" https://78402688480b.ngrok-free.app "]
# whatever running in Https, we will be able to access it. If this URL I am going to share to anyone, if people try to start hiting
# all public will be able to access it.
# we have to give a proper Route. 
# This is my Route -> [ http://127.0.0.1:8000/Vijay/gurung/xyz?a=4&b=5 ]
# Means till this point Url will going to work - ("http://127.0.0.1:8000") now let me make some changes, replace with the 
# Terminal URL with my this url, so below is the full final Route ->
# [ https://00d8867eaec6.ngrok-free.app/Vijay/gurung/xyz?a=4&b=5  ]

# copy this URL and paste in Brower and it will show that -> ("Visit site") if we anybody copy and paste there brower.
# He or she can enter my server now.

# Note : 
# To stop this live URL just go to the Terminal and ( "CTRL+C" ). it will stop.

# We have created our very 1st API.

# Next,

# While creating API, there is multiple concept exit, lets discussed this.

# [POST]

# we have written "@app.get"  & There is another testing tool called -> "PostMan"

# "PostMan" mostly people prefer because developer create thousand of API, they have to maintain those "Logs & APIs".

# "POSTMAN" : is basically a tool which keep everything in one place. Multiple way for testing and hitting the API.
# There is not only the "POSTMAN". but yeah good tool most prefer it.

# Lets download Postman URL : [ https://www.postman.com/downloads/ ]


# Lets open this "Postman"

# Here Select ["GET"] : Paste code : [ http://localhost:8000/Vijay/gurung/xyz?a=7&b=9 ]

# Lets give Key Value :  Key = a & b and Value = 7 & 9  outcome is [ 16 ] & then right corner send or execute this code. As a outcome we can see 
# then, I am able to get the outcome.
# This is something like, I am sending the Request & I am geeting the some short of outcome.
# even with the "PostMan", I am abel to test it.
# This is something, I am sending the request and I am geeting the output.

# what benefit of this platform is that : its help us managing the mutiple environment, multiple flows and team.

# when we create a "API", we create thousand of API's. not just one. there will be thousand of functions, "different 
# requirement". Then we have to exposed each and everything. 

# when the number APIs keep increasing then, it haard to manage.

# This is my API - [http://localhost:8000/Vijay/gurung/xyz] <- at this URL or at this API's, my function is avaiable.

# Note :  ["Euron.Ai"]
# Similary, this is the for example : Euron API key where this is located : ["https://api.euron.one/api/v1/euri/chat/completions" ]
# This is basically the system - "( https://api.euron.one/  )" & tecnically this is a "Route". -> [ "api/v1/euri/chat/completions"]
# at this folder it is running

# Similary, this is my system, help me out to reach out to the system -> ("http://localhost:8000/") &
# Inside the system at this location ["/Vijay/gurung/xyz"], at this Route it is running.


# Note : 

# Lets say I want to check or hit with the help of "Curl" then, open the terminal and type :
# type -> curl "http://localhost:8000/Vijay/gurung/xyz?a=7&b=9"

# Yes, even with the help of the "Curl", I am able to hit it. Becasue this is API.

# Note :  ["GET"] method,  what is the meaning of it?

# Answer : GET means we are trying to get the, But there is technical meaning to it, GET simply mean that, we are trying to
# send a data, which will be expose, to the world, entire world will be able to see your data. This is another meaning if this.
# How ?

# Note :  Google search ("Data Sciene")
# 
# Lets say - I went to Google and search for the "Data science", after seach, we can observed the URL.

# https://www.google.com/search?q=data+science& 

# Technically, it was a   whatever data I am trying to send this is visiable to the entire world.

# Note : ("Gmail")

# search for gmail.com on Google, and trying to type email and password & if we observed the URL of this.
# we try to pass our email id and Password, can we see the data inside my URL like my email and password.No we can't see.

# Basically, when we are trying to Signup, that time we are sending our data our email and Password.
# Similay, when we try to login "Euron" platform or any other plateform, which mean by providing email and Password, then we 
# received the OTP or Google login,. so with the help of google any platform will authorized.

# Note : 

# 1.So, one of this case the URL, that "Data Science" one is visibale for entire world.
# 2.But for the other case "Gmail" one, it is not visiable. As we can say this one Secured one.

# Whever my dataset is visiable, its called as "GET" request & its not secured.

# Similar way, Gmail login, we are sending a data, which is called as ["POST"], means we are attaching our data, as a body
# in Body we are trying to attached the data then we are sending a data, so thatit will not visiable to the "outer world or 
# to the any user.like what we are sending, we have to provide its a rsecured data.

# S, the 2 differnece, we are able to find out. One is ["GET"] & another is ["POST"]
# "GET" is non secured and other side, POST is sending a data via a body whic is technically  a recured one.

# Note :

# How I will be able to create a POST API

# Continue : 1:33:40




# Lets understand - How I can send a Post and that will be secure and eventually we will going to understand how we ar going 
# to even test those part via "CURL" via a "POSTMAN", how I will be able to do it. Lets tryt to understand this.

# ["GET"] is a unsecure way to send a data,
# For example :  
# when we do a Google search, it actually a Get, we are sending a data, we are hitting a google search. that is basically a goole
# search, in a response, it will give me a list of the pages or outcomes. It executing some function, it try to do some sort of
# a search function. That search function will try to search those pages, the revelant pages, based on the query and then we get
# that data, this is actually what happened.

# Now Let create a another function : 

# Let say ["Substract"] function, I am going to create. Substract again going to take 2 data which is ("a & b") & it will going
# return (a & b)


from fastapi import FastAPI

app = FastAPI()

@app.get("/Vijay/gurung/xyz")
def add(a:int,b:int):  
    return a+b


@app.post("/subtract")
def substract(a:int,b:int):
    return a-b

print(add(3,4))




# Now I have to convert this function, as a API. So, that it will be able to do something. It will take 2 inputs and substract it
# & It will give the output, Now let say I have to convert as an API, we know this manner "@app.get("/Vijay/gurung/xyz")"
#  we are able to convert the API.

# ["GET"] means whenever I am sending a data, it will be exposed, & we are able to see, we are here attacting our data 
# into a URL : "Vijay/gurung/xyz", So then we are trying to do a this kind of request. Otherwise we were not able to do the request
# SO, secure way will be ["POST"] - we have to convert this entire thing as a post.
# So, I can call @app."POST" and then I can give my Path, whatever path I want I can give lets say ["subtract"], I have 
# given this path a "subtract" & I am assuiming this will expose.
# 1st Save it - CRTL + S and now lets try to test it.


# Now lets go to the URL open into the browser : ["http://localhost:8000 "] or ("http://127.0.0.1:8000"). lets take a 
# -> this one -> ["http://localhost:8000/docs "].

# Now, we can see that there is 2 function.
# One is hosted at this URL : ("/Vijay/gurung/xyz") that was the -["GET"] one. 
# Then, I have a second one is -> ["POST"].This Substraction function avaiable at ("/subtract")
# which I have written at this "Route".
# This time also, I will put the "a" value as 5 and "b" value as 2. If I will execute, below outcome we can see that
# Reponse :  Curl and  Response body = ("3") outcome we can see.


# 2 function, I have written "Addition" & "Substraction" 

# 1.Now, I will put the Vlaue in Addiction : a = 4 and b = 5 and outcomes is ("9") with "GET"
# 2.For "Substraction" the value, I have given was : a = 5 and b = 2. the outcome is ("3") with "POST"
# we can see in the both below the "Curl" that, "GET" & "POST" this is the only difference we can see or Observed.

# Both the cases, I am able to get the data. How this 2 things is differnce?  obvioulsy one is "GET" & "POST".

# Note :

# Let's do the same as we did previously for addition, lets copy the URL.
# of the Substraction URL : ["http://localhost:8000/subtract?a=5&b=2"]  & hit enter, we can see the result, Method not allowed
# But the addition case, it was giving me the ("9"). this is difference we can see.

# So, here in this "substraction". I have to expose the data URL : ["http://localhost:8000/substraction?a=5&b=2"]
# I am trying to expose the data, because I have to send the data, "5-2", to execute this function, If I am not sending the data,
# the function will not be executed.Now when I am sending a data, it is telling me no it is not allowed "Method not allowed",
# you are not suppose to allowed to expose your data, into the URL, this is what it is trying to say.

# Because, we have created this Subtract function, exposed via a "POST" not via a "GET", that is the differnce between the 
# "GET" & "POST" - Both the way I am trying to expose my data. only differnec is that, one is allowing and another is not allowing
# through the URL. But Yes I will be able to test it in the "POSTMAN". BUt I tested but same outcome.

# I am call it in the "POSTMAN", "CURL" or any programing but in the URL it is not allowed.
# 
# because I have created this function, which is hosted at this particular URL : "http://localhost:8000/subtract".
# In nature it is actually a "POST". which means you should not pass any data, as a exposed one. 
# You should pass a data in a body.



# Note : POSTMAN : POST | 

# Lets do to later some Error message we are getting on this

# So, How I will be able to Test it. Through a "POSTMAN", Lets try to test it.

# Select as a ("POST") - http://localhost:8000/ <- means system and "substraction" <- it means function.
# 
# This time select : POST : paste the URL : "http://localhost:8000/subtract"  & this time dont put the "parameter"
# select the "BODY" next -> "ROW" & here select JSON format -> means "Key" & "Value" format.
# {
#    "a" : 6,
#    "b" : 2
# }

# Note :  ["Curl"] :

# Lets try to hit from "Curl", 
# Just open the "Cmd" and paste this code I copied from that URL of "substraction" where "Curl" in mentioned. 

#  [ curl -X 'POST' 'http://localhost:8000/subtract?a=5&b=2' ]
# I tried to hit, it is not working as a outcome we can see, we was trying to do in a old fashion.
# Incase of the "GET", everything was working, but when I started doing with the "POST", it started giving me a Error.
# Both "Curl" & "POSTMAN", this case it is not working.

# How we will fix this, how we can make it running ?

# There is something is called the "Pidentic", I have to handle with that, I can make it working.

# "Pydantic" :  

# ["from Pydantic import BaseModel"]
# 
#  means again a Set of the rule a libary, whihc try to give us set of a rule, by which we will be able to set a data Type
# in a "Pydantic" way.

# How we can do a Implementation ? 
# For that we have to call the "Pydantic" from Pidentic & then we have to import the Baseclass is "BassModel"


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/Vijay/gurung/xyz")
def add(a:int,b:int):  
    return a+b



class subtractmodel(BaseModel):
    a:int
    b:int

def substract(a:int,b:int):
    return a-b

@app.post("/substract")
def substract_numbers(model:subtractmodel):
    return substract(model.a, model.b)

print(add(3,4))



# And How I will be able to use this "Pydantic"? 

# For this lets try to create our own class, so "Subtract medel" let suppose I am trying to create,  inherit this base model.
# so, that, my custom class would not be having idea about this entire rule & Regulation.

# Here I know, I am going to pass basically, "a" & "b" both as a "Integer", I am going to pass.

# I have just define the "a = integer & b = integer", whenever, we are goign to send a data, it will be looking for validation.
# "a" should always be "int" & "b" should be always "int". This "Pydantic" class whihc I am trying to create, ans I am trying to
# allign with "Pydantic" rule, it is just going to help me out interm of validation, nothing else.

# which is required for "POST", for the "GET", it is not required.

# As "POST", is a more secure one, so we have to attached the "Pydantic" over here & with the help of this "Pydantic",
# we will be able to achive. Lets try this out.

# So, I have created simple subtract function:

# def substract(a:int,b:int):
#    return a-b

# How, it will be able to understand that use a "Pydantic", for this try to create another function.

# def substract_numbers(model:substrctmodel):
#    return substract(model.a, model.b)

# in return "Subtract" function we are trying to call. which needs "a" & "b". So, we are trying to call "Model.a" & "Model.b"

# This is my original funtion  ;

# def substract(a:int,b:int):
#    return a-b

# I am trying to call this original function :"substract"

# def substract_numbers(model:substrctmodel):
#    return substract(model.a, model.b)

# Now this orginal function take the 2 input ["a" & "b"], but how, 1st of all.

# the data will come to here - 
# class subtractmodel(BaseModel):
#    a:int
#    b:int

# it will validate here in "a & b". This is a "Pydantic" implementation. It will validate,  ("a = int & b = int") - whether it is 
# integer (int) or not?

# "Pydantic" is a another libary, which will going to help me with data validation.
# In the "Langchain" "Langgraph" & "Lama indexes", we will end up using this multiple time.

# if the data somebody has passed & data is in the some other format. It will not be accepted. once it will passed over here.

# once it passed over here -  
# 
# def substract_numbers(model:substrctmodel):
# return substract(model.a, model.b)

# I am trying to create a function, & I am trying to give a access to the "subtractmodel"

# Now this "model" & "model.a" variable, whichever data, which came here, 

# class subtractmodel(BaseModel):
#    a:int
#    b:int

# Just try to access, "a" out of it, and "b" outcome. This is called the "Pydantic" implement which  I am using for data validation.

# Now once created it Expose like a "API" - so, @app.post("/subtract")

# This is the function:

 #def substract_numbers(model:substrctmodel):
#    return substract(model.a, model.b)

# which avaiable at this "API" at ["@app.get("/Vijay/gurung/xyz"].

# This is basically calling my orginal function  : 

# def substract(a:int,b:int):
#    return a-b

# NOw techically using a "Pydantic".

# Now "CTRL + S" save it.

