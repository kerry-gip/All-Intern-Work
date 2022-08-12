#queries

from collections import namedtuple


{
    allPersons{
        name 
        age 
        posts{
            title
        }
    }
}

{
    "allPersons": [
        {"name": "Johnny"};
        {"name": "Sarah"},
        {"name": "Alive"}
    ]
}

{
    allPersons(last:2){
        name 
        #returns only specfic number of people, takes last 2 people 
    }
}

#mutations
mutation{
    createPerson(name:"Bob", age:36){
        name 
        age 
        
    }
}

#create person
"createPerson":{
    "name": "Bob",
    "age": 36,
}


type Person{
    id : ID!
    name: String!
    age: Int!
}

mutation{
    createPerson(name: "Alice", age: 36){
        id
    }
    
}

#realtime update with subscriptions
Subscription{
    newPerson{
        name 
        age 
    }
}

#new mutation on a subsciption
"newPerson":{
    "name": "Jane",
    "age" : 23
}

