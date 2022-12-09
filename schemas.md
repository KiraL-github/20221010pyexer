MODEL / DB FIELDS

//  ! database
// advantage of django : build up database with simple codes
// advantage of django : build-in admin site

#### LISTING
id : INT
realtor : INT (FOREIGN KEY [realtor])
title : STR
address : STR
city : STR
state : STR
zipcode : STR
description : TEXT
price : INT
bedrooms : INT
bathroom : INT
garage : INT [0] // [ ] - default value // 0 means false
sqft : INT
lot_size : FLOAT
is_published : BOOL [true]
list_data : DATE
photo_main : STR
photo_1 : STR
photo_2 : STR
photo_3 : STR
photo_4 : STR
photo_5 : STR
photo_6 : STR

### REALTOR
id : INT
name : STR
photo : STR
description : TEXT
email : STR
phone : STR
is_mvp : BOOL [0]
hire_date

### CONTACT

